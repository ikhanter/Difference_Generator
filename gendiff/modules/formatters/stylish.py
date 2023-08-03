"""Module for building diff-string for two JSON files processed by form_diff function."""  # noqa: E501
from gendiff.modules.formatters.changebool import change_bool

PREFIX = '{'
REPLACER = '    '
REPLACER_PLUS = '  + '
REPLACER_MINUS = '  - '
SUFFIX = '}'


def stylish_diff(diff):  # noqa: WPS210
    """
    Generate string with diff for two JSON/YAML files.

    Args:
        diff (dict): dict with statuses of keys

    Returns:
        str: Complex string contains diff
    """
    lines = []
    depth = 1

    def form_lines(item, sign, depth, value='actual'):

        def form_dict(dict_item, depth):
            for key, val in dict_item.items():
                if isinstance(val, dict):
                    lines.append(f"{REPLACER * depth}{key}: {PREFIX}")
                    form_dict(val, depth + 1)
                    lines.append(f"{REPLACER * depth}{SUFFIX}")
                else:
                    lines.append(f"{REPLACER * depth}{key}: {change_bool(val)}")  # noqa: E501

        if value == 'old':
            main_key = 'old_value'
        else:
            main_key = 'actual_value'
        if isinstance(item[main_key], dict):
            lines.append(f"{REPLACER * (depth - 1)}{sign}{item['key']}: {PREFIX}")  # noqa: E501
            form_dict(item[main_key], depth + 1)
            lines.append(f"{REPLACER * depth}{SUFFIX}")
        else:
            lines.append(f"{REPLACER * (depth - 1)}{sign}{item['key']}: {change_bool(item[main_key])}")  # noqa: E501

    def add_element(source, depth):
        sign = REPLACER
        match source['status']:
            case 'added':
                sign = REPLACER_PLUS
            case 'removed':
                sign = REPLACER_MINUS
            case 'updated':
                form_lines(source, REPLACER_MINUS, depth, 'old')
                sign = REPLACER_PLUS
        form_lines(source, sign, depth, 'actual')

    def walk(inner_diff, depth, init):
        if init:
            init += ': '  # noqa: WPS336
        lines.append(f'{REPLACER * (depth - 1)}{init}{PREFIX}')
        for element in inner_diff:
            if isinstance(element['actual_value'], list):
                walk(element['actual_value'], depth + 1, element['key'])
            else:
                add_element(element, depth)
        lines.append(f'{REPLACER * (depth - 1)}{SUFFIX}')

    walk(diff, depth, '')
    return '\n'.join(lines)
