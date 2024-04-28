from gendiff.comparator import compare_data
from gendiff.formatters.format_selection import choose_formatter
from gendiff.parser import parser


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    raw_data = compare_data(data1, data2)
    return choose_formatter(raw_data, format_name)
