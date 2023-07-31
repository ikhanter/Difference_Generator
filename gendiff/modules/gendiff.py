"""Module for finding diffs between two json-files."""


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


def form_diff(data1, data2):
    """
    Form new dict with nested structure for 2 JSON files.

    Args:
        data1 (dict): JSON-file as dict
        data2 (dict): JSON-file as dict

    Returns:
        dict: New dict which contains nested structure
    """
    diff = {}

    def walk(value1, value2, diff_dict):
        all_keys = take_keys(value1, value2)
        for key in all_keys:
            if key in value1.keys():
                if key in value2.keys():
                    if isinstance(value1[key], dict) and isinstance(value2[key], dict):  # noqa: E501
                        diff_dict[key] = {}
                        walk(value1[key], value2[key], diff_dict[key])
                    elif value1[key] == value2[key]:
                        diff_dict[key] = 'unchanged'
                    else:
                        diff_dict[key] = 'changed'
                else:
                    diff_dict[key] = 'removed'
            else:
                diff_dict[key] = 'added'

    walk(data1, data2, diff)
    return diff
