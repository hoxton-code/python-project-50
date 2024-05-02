import json
import yaml


def get_file_format(file_path):
    """
    Identify the file format from its extension.

    Parameters:
    file_path (str): File path to determine format.

    Returns:
    File format ('json' or 'yaml').
    """
    if file_path.endswith('.json'):
        return 'json'
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return 'yaml'


def file_parser(file_path):
    """
    Parse JSON or YAML file and return data.

    Parameters:
    file_path (str): File path to parse.

    Returns:
    Parsed file data as a dictionary.
    """

    file_format = get_file_format(file_path)

    if file_format == 'json':
        with open(file_path) as file:
            data = json.load(file)
            return data
    elif file_format == 'yaml':
        with open(file_path) as file:
            data = yaml.safe_load(file)
            return data
    else:
        raise ValueError("Unsupported file format for file")
