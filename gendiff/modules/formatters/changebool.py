"""Module for changing post-processed boolean data after using json-module to original JSON values."""  # noqa: E501


def change_bool(source):
    """
    Change source values after json-module processing to original JSON values.

    Args:
        source (value): JSON-source

    Returns:
        source or bool: Changed initial source
    """
    if source is None:
        return 'null'
    elif source is True:
        return 'true'
    elif source is False:
        return 'false'
    return source
