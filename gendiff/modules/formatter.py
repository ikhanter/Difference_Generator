"""Module for building diff-string for two JSON files processed by form_diff function."""  # noqa: E501
PREFIX = '{'
REPLACER = '    '
REPLACER_PLUS = '  + '
REPLACER_MINUS = '  - '
SUFFIX = '}'


def generate_diff(data1, data2, diff):  # noqa: WPS210
    """
    Generate string with diff for two JSON/YAML files.

    Args:
        data1 (dict): JSON-file as dict
        data2 (dict): JSON-file as dict
        diff (dict): nested structure with changed in data1 relatively data2

    Returns:
        str: Complex string contains diff
    """
    lines = []
    depth = 0

    def add_element(source, init, sign, depth, change=False):
        sign_before = REPLACER
        if change:
            sign_before = sign
        if isinstance(source, dict):
            lines.append(f'{REPLACER * (depth - 1)}{sign_before}{init}: {PREFIX}')  # noqa: E501
            for key in source.keys():
                add_element(source[key], key, sign, depth + 1)
            lines.append(f'{REPLACER * depth}{SUFFIX}')
        else:
            lines.append(f'{REPLACER * (depth - 1)}{sign_before}{init}: {source}')  # noqa: E501

    def walk(value1, value2, inner_diff, depth, init):
        if init:
            init += ': '  # noqa: WPS336
        lines.append(f'{REPLACER * depth}{init}{PREFIX}')
        for key in inner_diff.keys():
            if isinstance(inner_diff[key], dict):
                walk(value1[key], value2[key], inner_diff[key], depth + 1, key)
            match inner_diff[key]:
                case 'changed':
                    add_element(value1[key], key, REPLACER_MINUS, depth + 1, change=True)  # noqa: E501
                    add_element(value2[key], key, REPLACER_PLUS, depth + 1, change=True)  # noqa: E501
                case 'added':
                    add_element(value2[key], key, REPLACER_PLUS, depth + 1, change=True)  # noqa: E501
                case 'removed':
                    add_element(value1[key], key, REPLACER_MINUS, depth + 1, change=True)  # noqa: E501
                case 'unchanged':
                    add_element(value1[key], key, REPLACER, depth + 1)
        lines.append(f'{REPLACER * depth}{SUFFIX}')

    walk(data1, data2, diff, depth, '')
    return '\n'.join(lines)
