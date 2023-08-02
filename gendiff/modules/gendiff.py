"""Module for finding diffs between two json-files."""
from gendiff.modules.formatters.json import json_diff
from gendiff.modules.formatters.plain import plain_diff
from gendiff.modules.formatters.stylish import stylish_diff
from gendiff.modules.loader import read_pair_of_files


def generate_diff(data1, data2, format_name='stylish'):
    """
    Simplify script building for gendiff.

    Args:
        data1 (path): Path for the first file
        data2 (path): Path for the second file
        format_name (default='stylish', 'plain'): Representation format of the diff  # noqa: E501

    Returns:
        str: Multiline string of the diff
    """
    if format_name == 'stylish':
        return stylish_diff(*read_pair_of_files(data1, data2))
    elif format_name == 'plain':
        return plain_diff(*read_pair_of_files(data1, data2))
    elif format_name == 'json':
        return json_diff(*read_pair_of_files(data1, data2))
