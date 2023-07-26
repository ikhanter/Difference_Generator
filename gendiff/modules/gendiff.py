"""Module for finding diffs between two json-files."""
import json


def stringify(data1, data2, keys):
    """
    Make JSON string with marked changes.

        Parameters:
            data1 (dict): JSON formed as a dict
            data2 (dict): JSON formed as a dict
            keys (list): List of all keys for two JSON files

        Returns:
            String of merged JSON files with marked changes
    """
    prefix = '{'
    suffix = '}'
    lines = []
    lines.append(prefix)
    for key in keys:
        if (key in data1.keys()) and (key in data2.keys()):
            if data1[key] == data2[key]:
                lines.append(f'   {key}: {data1[key]}')
            else:
                lines.append(f' - {key}: {data1[key]}')
                lines.append(f' + {key}: {data2[key]}')
        elif (key in data1.keys()) and (key not in data2.keys()):
            lines.append(f' - {key}: {data1[key]}')
        elif (key not in data1.keys()) and (key in data2.keys()):
            lines.append(f' + {key}: {data2[key]}')
    lines.append(suffix)
    return '\n'.join(lines)


def read_json(file1, file2):
    """
    Read JSON files as dict.

        Parameters:
            file1: Path to JSON-file
            file2: Path to JSON-file

        Returns:
            Tuple of two JSON objects as dicts
    """
    with open(file1) as data1:
        with open(file2) as data2:
            f1 = json.load(data1)
            f2 = json.load(data2)
    return f1, f2


def generate_diff(json1, json2):
    """
    Treat keys from both JSON files for usage in stringify in future.

        Parameters:
            json1: JSON file as a dict
            json2: JSON file as a dict

        Returns:
            String of merged JSON files with marked changes
    """
    keys_f1 = set(json1.keys())
    keys_f2 = set(json2.keys())
    all_keys = sorted(keys_f1.union(keys_f2))
    return stringify(json1, json2, all_keys)
