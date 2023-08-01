"""Module for finding diffs between two json-files."""
from gendiff.modules.formatters.plain import plain_diff
from gendiff.modules.formatters.stylish import stylish_diff


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
        return stylish_diff(data1, data2)
    elif format_name == 'plain':
        return plain_diff(data1, data2)
