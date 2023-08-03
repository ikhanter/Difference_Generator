"""Module for plain representation of diff."""
from gendiff.modules.formdiff import form_diff
from gendiff.modules.formatters.changebool import change_bool

def plain_diff(data1, data2, diff):
    """
    Generate diff in a plain style.

    Args:
        data1 (dict): 1st JSON/YAML file as dict
        data2 (dict): 2nd JSON/YAML file as dict

    Returns:
        str: Multiline string with diff between two files
    """
    lines = []
    inner_path = ''

    def add_element(value_main, action, path, *value_opt):
        temp = ''

        def check_element(value):
            nested_structures = (list, dict, tuple, set)
            bool_structures = ('true', 'false', 'null')
            new_value = change_bool(value)
            if isinstance(new_value, str):
                if new_value in bool_structures:
                    return f'{new_value}'
                return f"\'{new_value}\'"
            elif type(new_value) in nested_structures:  # noqa: WPS516
                return '[complex value]'
            return f'{new_value}'

        if action == 'updated':
            before = check_element(value_main)
            after = check_element(value_opt[0])
            temp = f'. From {before} to {after}'
        elif action == 'added':
            added = check_element(value_main)
            temp = f' with value: {added}'
        lines.append(f"Property \'{path[:-1]}\' was {action}{temp}")

    def walk(value1, value2, inner_diff, inner_path):
        for key in inner_diff.keys():
            in_path = f'{inner_path}{key}.'
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
