"""JSON-style formatter for diff."""
import json


def json_diff(diff):
    """
    Make JSON representation of diff.

    Args:
        diff (dict): dict with statuses of keys

    Returns:
        list: JSON representation of diff between two files
    """
    return json.dumps(diff, indent=2)
