from gendiff.comparator import compare_data
from gendiff.formatters import choose_formatter
from gendiff.file_parser import file_parser


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
     Generate a formatted diff between two files.

     Parameters:
     file_path1 (str): Path to the first file.
     file_path2 (str): Path to the second file.
     format_name (str, optional): Formatter name. Defaults to 'stylish'.

     Returns:
     Formatted diff string.
     """

    data1 = file_parser(file_path1)
    data2 = file_parser(file_path2)
    raw_data = compare_data(data1, data2)
    return choose_formatter(raw_data, format_name)
