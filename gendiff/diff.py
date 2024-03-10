import core


def generate_diff(file_path1, file_path2):
    data1 = core.open_file(file_path1)
    data2 = core.open_file(file_path2)
    keys = sorted(set(data1.keys()) | set(data2.keys()))

    diff_list = []
    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if isinstance(value1, bool):
            value1 = str(value1).lower()
        if isinstance(value2, bool):
            value2 = str(value2).lower()

        if value1 == value2:
            diff_list.append(f'    {key}: {value1}')
        elif value1 is None:
            diff_list.append(f'  + {key}: {value2}')
        elif value2 is None:
            diff_list.append(f'  - {key}: {value1}')
        else:
            diff_list.append(f'  - {key}: {value1}')
            diff_list.append(f'  + {key}: {value2}')

    formatted_diff = '{\n' + '\n'.join(diff_list) + '\n}'
    return formatted_diff


file1_path = '../files/file1.json'
file2_path = '../files/file2.json'
diff = generate_diff(file1_path, file2_path)
print(diff)
