def add_changes(key, state, value, result_dict):
    result_dict[key] = {
        # 'name': key,
        'state': state,
        'value': value,
    }


def get_value(data):
    return data.get('value', data) if isinstance(data, dict) else data


def get_state(data):
    return data.get('state', None) if isinstance(data, dict) else data


def compare_data(dict1, dict2):
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
            add_changes(key, 'changed, nested', compare_data(dict1[key], dict2[key]), result)
        else:
            diff_dict = {'old_value': dict1[key], 'new_value': dict2[key]}
            add_changes(key, 'changed', diff_dict, result)
    return result
