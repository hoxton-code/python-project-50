import json


def open_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
    return data
