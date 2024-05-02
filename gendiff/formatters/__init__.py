from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import format_json


def choose_formatter(data, formatter=None):
    """
    Apply a specified formatter to data, defaulting to 'stylish'.

    Parameters:
    data: Data to format.
    formatter (str, optional): Formatter name. Defaults to 'stylish'.

    Returns:
    Formatted data.
    """

    formatter = formatter or 'stylish'
    formatters = {'stylish': stylish, 'plain': plain, 'json': format_json}
    return formatters[formatter](data)
