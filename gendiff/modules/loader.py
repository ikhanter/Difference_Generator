"""Module for load and process initial JSON/YAML files into dict."""
import json

import yaml


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
