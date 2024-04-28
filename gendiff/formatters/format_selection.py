from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import format_json


def choose_formatter(data, formatter=None):
    formatter = formatter or 'stylish'
    formatters = {'stylish': stylish, 'plain': plain, 'json': format_json}
    return formatters[formatter](data)
