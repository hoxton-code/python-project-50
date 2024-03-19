from gendiff.core import open_file


def compare_values(key, value1, value2):
    if value1 == value2:
        return f'    {key}: {value1}'
    elif value1 is None:
        return f'  + {key}: {value2}'
    elif value2 is None:
        return f'  - {key}: {value1}'
    else:
        return f'  - {key}: {value1}\n  + {key}: {value2}'


def generate_diff(file_path1, file_path2):
    data1 = open_file(file_path1)
    data2 = open_file(file_path2)
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_list = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if isinstance(value1, bool):
            value1 = str(value1).lower()
        if isinstance(value2, bool):
            value2 = str(value2).lower()

        diff_list.append(compare_values(key, value1, value2))

    formatted_diff = '{\n' + '\n'.join(diff_list) + '\n}'
    return formatted_diff


# file1_path = '../files/file1.json'
# file2_path = '../files/file2.json'
# diff = generate_diff(file1_path, file2_path)
# print(diff)
