"""Module for finding diffs between two json-files."""
from gendiff.modules.formatters.json import json_diff
from gendiff.modules.formatters.plain import plain_diff
from gendiff.modules.formatters.stylish import stylish_diff
from gendiff.modules.formdiff import form_diff
from gendiff.modules.loader import read_pair_of_files


def generate_diff(path1, path2, format_name='stylish'):
    """
    Simplify script building for gendiff.

    Args:
        path1 (path): Path for the first file
        path2 (path): Path for the second file
        format_name (default='stylish', 'plain', 'json'): Representation format of the diff  # noqa: E501

    Returns:
        str: Multiline string of the diff
    """
    f1, f2 = read_pair_of_files(path1, path2)
    diff = form_diff(f1, f2)
    if format_name == 'stylish':
        return stylish_diff(diff)
    elif format_name == 'plain':
        return plain_diff(diff)
    elif format_name == 'json':
        return json_diff(diff)
