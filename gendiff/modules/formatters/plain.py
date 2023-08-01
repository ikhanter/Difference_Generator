"""Module for plain representation of diff"""
from gendiff.modules.gendiff import form_diff


def plain_diff(data1, data2):
    diff = form_diff(data1, data2)
    lines = []
    inner_path = ''

    def add_element(value_main, action, path, *value_opt):
        temp = ''

        def check_element(value):
            nested_structures = (list, dict, tuple, set)
            bool_structures = ('true', 'false', 'null')
            if isinstance(value, str):
                if value in bool_structures:
                    return f'{value}'
                return f'\'{value}\''
            elif type(value) in nested_structures:
                return f'[complex value]'
            else:
                return f'{value}'

        if action == 'updated':
            before = check_element(value_main)
            after = check_element(value_opt[0])
            temp = f'. From {before} to {after}'
        elif action == 'added':
            added = check_element(value_main)
            temp = f' with value: {added}'
        lines.append(f'Property \'{path[:-1]}\' was {action}{temp}')

    def walk(value1, value2, inner_diff, inner_path):
        for key in inner_diff.keys():
            in_path = inner_path + f'{key}.'
            if isinstance(inner_diff[key], dict):
                walk(value1[key], value2[key], inner_diff[key], in_path)
            match inner_diff[key]:
                case 'updated':
                    add_element(value1[key], 'updated', in_path, value2[key])
                case 'added':
                    add_element(value2[key], 'added', in_path)
                case 'removed':
                    add_element(value1[key], 'removed', in_path)

    walk(data1, data2, diff, inner_path)
    return '\n'.join(lines)
