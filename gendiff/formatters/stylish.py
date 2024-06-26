from gendiff.comparator import get_value, get_state
from itertools import chain


def to_str(value, depth):
    """
     Convert a value to a string, format dictionaries with stylish.

     Parameters:
     value: Value to convert.
     depth (int): Nesting depth for indentation.

     Returns:
     String representation of the value.
     """
    return stylish(value, depth) if isinstance(value, dict) else (
        convert_bool_value(str(value)))


def convert_bool_value(string):
    """
     Convert Python boolean and None values to their JSON string equivalents.

     Parameters:
     string (str): The string representation of a Python value.

     Returns:
     str: The JSON string equivalent of the Python boolean or None value.
     """
    replacements = {'None': 'null', 'True': 'true', 'False': 'false'}
    return replacements[string] if string in replacements else string


def stylish(dict_diff, depth=0, number_indents=4, indent_symbol=' '):
    """
    Render a diff dictionary into a stylish format.

    Parameters:
    dict_diff (dict): Diff to format.
    depth (int, optional): Nesting depth for indentation. Defaults to 0.
    number_indents (int, optional): Indent symbols per level. Defaults to 4.
    indent_symbol (str, optional): Indentation symbol. Defaults to ' '.

    Returns:
    Formatted diff string.
    """

    indent = (indent_symbol * number_indents) * depth
    result_tree = []

    for key, val in dict_diff.items():
        value = get_value(val)
        state = get_state(val)
        indent_added = f'{indent}  + {key}'
        indent_remove = f'{indent}  - {key}'
        indent_unchanged = f'{indent}    {key}'

        if state == 'changed':
            str_old_val = (f"{indent_remove}: "
                           f"{to_str(value['old_value'], depth + 1)}")
            str_new_val = (f"{indent_added}: "
                           f"{to_str(value['new_value'], depth + 1)}")
            string = f"{str_old_val}\n{str_new_val}"
        elif state == 'removed':
            string = f"{indent_remove}: {to_str(value, depth + 1)}"
        elif state == 'added':
            string = f"{indent_added}: {to_str(value, depth + 1)}"
        else:
            string = f"{indent_unchanged}: {to_str(value, depth + 1)}"

        result_tree.append(string)
    result = chain("{", result_tree, [indent + "}"])
    return '\n'.join(result)
