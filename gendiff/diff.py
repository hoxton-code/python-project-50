from gendiff.comparator import compare_data
from gendiff.stylish import stylish
from gendiff.parser import parser


def generate_diff(file_path1, file_path2):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    raw_data = compare_data(data1, data2)
    return stylish(raw_data)


# file1_path = '../tests/fixtures/file_nested1.yaml'
# file2_path = '../tests/fixtures/file_nested2.yaml'
# diff = generate_diff(file1_path, file2_path)
# print(diff)
