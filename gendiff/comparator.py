def add_changes(key, state, value, result_dict):
    """
    Record a change in the result dictionary.

    Parameters: key (str): Change-associated key. state (str): Change state
    ('added', 'removed', 'changed', 'nested', 'unchanged'). value:
    Change-related value. result_dict (dict): Dictionary to record the change.

    Returns:
    None
    """
    result_dict[key] = {
        'state': state,
        'value': value,
    }


def get_value(data):
    """
    Get 'value' from data if it's a dictionary, or return data.

    Parameters:
    data: Data to extract 'value' from.

    Returns:
    'value' from data, or data itself if not a dictionary.
    """
    return data.get('value', data) if isinstance(data, dict) else data


def get_state(data):
    """
    Get 'state' from data if it's a dictionary, or return None.

    Parameters:
    data: Data to extract 'state' from.

    Returns:
    'state' from data, or None if not a dictionary.
    """
    return data.get('state', None) if isinstance(data, dict) else data


def compare_data(dict1, dict2):
    """
    Return the diff of two dictionaries.

    Parameters:
    dict1 (dict): First dictionary.
    dict2 (dict): Second dictionary.

    Returns:
    dict: Diff dictionary with changes, states, and values.
    """

    sorted_set_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = {}
    for key in sorted_set_keys:
        if key not in dict1:
            add_changes(key, 'added', dict2[key], result)
        elif key not in dict2:
            add_changes(key, 'removed', dict1[key], result)
        elif dict1[key] == dict2[key]:
            add_changes(key, 'unchanged', dict1[key], result)
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            add_changes(key, 'nested',
                        compare_data(dict1[key], dict2[key]), result)
        else:
            diff_dict = {'old_value': dict1[key], 'new_value': dict2[key]}
            add_changes(key, 'changed', diff_dict, result)
    return result
