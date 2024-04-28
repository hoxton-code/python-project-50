from gendiff.comparator import get_value, get_state


def convert_value(value):
    replacements = {'True': 'true', 'False': 'false', 'None': 'null'}

    if isinstance(value, dict):
        return '[complex value]'
    elif str(value) in replacements:
        return replacements[str(value)]
    return f"'{value}'"


def plain(dict_diff, path=''):
    result_str = []
    for key, val in dict_diff.items():
        value = get_value(val)
        state = get_state(val)
        current_path = path + key
        message = create_messages(state, value, current_path)
        if message:
            result_str.append(message)

    return '\n'.join(result_str)


def create_messages(state, value, path):
    message = ''
    if state == 'added':
        message += (
            f"Property '{path}' was added with value: {convert_value(value)}"
        )
    elif state == 'removed':
        message += f"Property '{path}' was removed"
    elif state == 'nested':
        message += plain(value, f"{path}.")
    elif state == 'changed':
        message += (
            f"Property '{path}' was updated. "
            f"From {convert_value(value['old_value'])} to "
            f"{convert_value(value['new_value'])}"
        )
    return message
