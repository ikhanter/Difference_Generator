"""Module for forming nested structure with info about diff between files."""


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
    diff = []

    def walk(value1, value2, diff_dict):
        all_keys = take_keys(value1, value2)
        for key in all_keys:
            new_value = {}
            new_value['key'] = key

            if key in value1.keys():
                if key in value2.keys():
                    if isinstance(value1[key], dict) and isinstance(value2[key], dict):  # noqa: E501
                        new_value['actual_value'] = []
                        walk(value1[key], value2[key], new_value['actual_value'])  # noqa: E501
                    elif value1[key] == value2[key]:
                        new_value['status'] = 'unchanged'
                        new_value['actual_value'] = value1[key]
                    else:
                        new_value['status'] = 'updated'
                        new_value['old_value'] = value1[key]
                        new_value['actual_value'] = value2[key]
                else:
                    new_value['status'] = 'removed'
                    new_value['actual_value'] = value1[key]
            else:
                new_value['status'] = 'added'
                new_value['actual_value'] = value2[key]
            diff_dict.append(new_value)

    walk(data1, data2, diff)
    return diff
