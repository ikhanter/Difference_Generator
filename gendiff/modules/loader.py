"""Module for load and process initial JSON/YAML files into dict."""
import json

import yaml


def transform_path_to_dict(path_name):
    """
    Take a file and transform to dict.

    Args:
        path_name (path): Path to JSON/YAML file

    Returns:
        dict: Dataset from file as dict
    """
    with open(path_name) as source:
        if path_name.endswith('.yml') or path_name.endswith('.yaml'):
            return yaml.safe_load(source)
        return json.load(source)


def read_pair_of_files(file1, file2):
    """
    Read JSON files as dict.

    Args:
        file1 (path): Path to file
        file2 (path): Path to file

    Returns:
        tuple: Tuple of two JSON objects as dicts
    """
    return transform_path_to_dict(file1), transform_path_to_dict(file2)  # noqa: E501
