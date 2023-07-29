"""Module for finding diffs between two json-files."""
import json

import yaml

PREFIX = '{'
REPLACER = '    '
REPLACER_PLUS = '  + '
REPLACER_MINUS = '  - '
SUFFIX = '}'


def generate_diff(data1, data2):  # noqa: C901
    """
    Make JSON string with marked changes.

    Args:
        data1 (dict): JSON formed as a dict.
        data2 (dict): JSON formed as a dict.

    Returns:
        str: String of merged JSON files with marked changes.
    """
    lines = []
    depth = 0
    lines.append(f'{REPLACER * depth}{PREFIX}')

    def add_one_dict(source: dict, init, depth, filler='    '):  # noqa: WPS442
        lines.append(f'{REPLACER * (depth - 1)}{filler}{init}: {PREFIX}')
        for key, val in source.items():  # noqa: WPS110
            if isinstance(val, dict):
                add_one_dict(val, key, depth + 1)
            else:
                lines.append(f'{REPLACER * (depth + 1)}{key}: {str(val)}')
        lines.append(f'{REPLACER * (depth)}{SUFFIX}')

    def walk(value1, value2, keys, depth):  # noqa: WPS442
        for key in keys:
            if key in value1.keys() and key in value2.keys():
                if isinstance(value1[key], dict):
                    if isinstance(value2[key], dict):
                        lines.append(f'{REPLACER * (depth + 1)}{key}: {PREFIX}')  # noqa: E501
                        walk(value1[key], value2[key], take_keys(value1[key], value2[key]), depth + 1)  # noqa: E501
                    else:
                        add_one_dict(value1[key], key, depth + 1, REPLACER_MINUS)  # noqa: E501
                        lines.append(f'{REPLACER * depth}{REPLACER_PLUS}{key}: {str(value2[key])}')  # noqa: E501
                elif isinstance(value2[key], dict):
                    lines.append(f'{REPLACER * depth}{REPLACER_PLUS}{key}: {str(value1[key])}')  # noqa: E501
                    add_one_dict(value2[key], key, depth + 1, REPLACER_PLUS)
                elif value1[key] == value2[key]:
                    lines.append(f'{REPLACER * (depth + 1)}{key}: {str(value1[key])}')  # noqa: E501
                else:
                    lines.append(f'{REPLACER * depth}{REPLACER_MINUS}{key}: {str(value1[key])}')  # noqa: E501
                    lines.append(f'{REPLACER * depth}{REPLACER_PLUS}{key}: {str(value2[key])}')  # noqa: E501
            elif key in value1.keys():
                if isinstance(value1[key], dict):
                    add_one_dict(value1[key], key, depth + 1, REPLACER_MINUS)
                else:
                    lines.append(f'{REPLACER * depth}{REPLACER_MINUS}{key}: {str(value1[key])}')  # noqa: E501
            else:
                if isinstance(value2[key], dict):
                    add_one_dict(value2[key], key, depth + 1, REPLACER_PLUS)
                else:
                    lines.append(f'{REPLACER * depth}{REPLACER_PLUS}{key}: {str(value2[key])}')  # noqa: E501
        lines.append(f'{REPLACER * depth}{SUFFIX}')
        return '\n'.join(lines)

    return walk(data1, data2, take_keys(data1, data2), depth)


def take_keys(data1, data2):
    """
    Form list of unique sorted keys for 2 JSON/YAML dict variables.

    Args:
        data1 (dict): JSON/YAML variable
        data2 (dict): JSON/YAML variable

    Returns:
        list: List of unique keys
    """
    keys1 = data1.keys()
    keys2 = data2.keys()
    return sorted(set((*keys1, *keys2)))  # noqa: C405


def read_pair_of_files(file1, file2):
    """
    Read JSON files as dict.

    Args:
        file1 (path): Path to file
        file2 (path): Path to file

    Returns:
        tuple: Tuple of two JSON objects as dicts
    """
    with open(file1) as data1:
        if file1.endswith('.yml') or file1.endswith('.yaml'):
            f1 = yaml.safe_load(data1)
        else:
            f1 = json.load(data1)

    with open(file2) as data2:
        if file2.endswith('.yml') or file2.endswith('.yaml'):
            f2 = yaml.safe_load(data2)
        else:
            f2 = json.load(data2)
    return change_bool(f1), change_bool(f2)


def change_bool(source):
    """
    Change source values after json-module processing to original JSON values.

    Args:
        source (json/dict): JSON-source

    Returns:
        source: Changed initial source
    """
    for key in source.keys():
        if isinstance(source[key], dict):  # noqa: WPS204
            change_bool(source[key])
        elif source[key] is None:
            source[key] = 'null'
        elif source[key] is True:
            source[key] = 'true'
        elif source[key] is False:
            source[key] = 'false'
    return source
