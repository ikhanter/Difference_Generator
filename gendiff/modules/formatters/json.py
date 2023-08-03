"""JSON-style formatter for diff."""
import json


def json_diff(data1, data2, diff):
    """
    Make JSON representation of diff.

    Args:
        data1 (dict): First JSON-file as a dict
        data2 (dict): Second JSON-file as a dict
        diff (dict): dict with statuses of keys

    Returns:
        list: JSON representation of diff between two files
    """

    def walk(value1, value2, inner_diff):

        def add_element(value, init, list_of_el, *values):
            new_values = []
            for val in values:
                if val == 'true':
                    new_values.append(True)
                elif val == 'false':
                    new_values.append(False)
                elif val == 'null':
                    new_values.append(None)
                else:
                    new_values.append(val)
            match value:
                case 'updated':
                    list_of_el.append({"key": init, "status": "updated", "old": new_values[0], "new": new_values[1]})  # noqa: Q000, E501
                case 'added':
                    list_of_el.append({"key": init, "status": "added", "value": new_values[0]})  # noqa: Q000, E501
                case 'removed':
                    list_of_el.append({"key": init, "status": "removed", "value": new_values[0]})  # noqa: Q000, E501
                case 'unchanged':
                    list_of_el.append({"key": init, "status": "unchanged", "value": new_values[0]})  # noqa: Q000, E501

        json_obj = []
        for key in inner_diff.keys():
            if isinstance(inner_diff[key], dict):
                json_obj.append({key: walk(value1[key], value2[key], inner_diff[key])})  # noqa: E501
            temp_values = []
            try:
                temp_values.append(value1[key])
            except KeyError:
                pass  # noqa: WPS420
            try:
                temp_values.append(value2[key])
            except KeyError:
                pass  # noqa: WPS420
            add_element(inner_diff[key], key, json_obj, *temp_values)
        return json_obj

    total = walk(data1, data2, diff)
    return json.dumps(total, indent=2)
