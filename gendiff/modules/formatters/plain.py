"""Module for plain representation of diff."""
from gendiff.modules.formatters.changebool import change_bool


def plain_diff(diff):
    """
    Generate diff in a plain style.

    Args:
        diff (dict): dict with statuses of keys

    Returns:
        str: Multiline string with diff between two files
    """
    lines = []
    inner_path = ''

    def add_element(source, path):
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

        if source['status'] != 'unchanged':
            if source['status'] == 'updated':
                before = check_element(source['old_value'])
                after = check_element(source['actual_value'])
                temp = f'. From {before} to {after}'
            elif source['status'] == 'added':
                added = check_element(source['actual_value'])
                temp = f' with value: {added}'
            lines.append(f"Property \'{path[:-1]}\' was {source['status']}{temp}")  # noqa: E501

    def walk(inner_diff, inner_path):
        for element in inner_diff:
            in_path = f"{inner_path}{element['key']}."
            if isinstance(element['actual_value'], list):
                walk(element['actual_value'], in_path)
            else:
                add_element(element, in_path)

    walk(diff, inner_path)
    return '\n'.join(lines)
