from gendiff.diff import generate_diff
import pytest


@pytest.mark.parametrize("file_path_1, file_path_2, format_name, "
                         "expected_output", [
                             ("tests/fixtures/file1.json",
                              "tests/fixtures/file2.json",
                              'stylish',
                              "tests/fixtures/expected_flat_output.txt"),
                             ("tests/fixtures/file1.yaml",
                              "tests/fixtures/file2.yaml",
                              'stylish',
                              "tests/fixtures/expected_flat_output.txt"),
                             ("tests/fixtures/file_nested1.json",
                              "tests/fixtures/file_nested2.json",
                              'stylish',
                              "tests/fixtures/expected_nested_output.txt"),
                             ("tests/fixtures/file_nested1.yaml",
                              "tests/fixtures/file_nested2.yaml",
                              'stylish',
                              "tests/fixtures/expected_nested_output.txt"),
                             ("tests/fixtures/file_nested1.json",
                              "tests/fixtures/file_nested2.json",
                              'plain',
                              "tests/fixtures/expected_plain_output.txt"),
                             ("tests/fixtures/file_nested1.yaml",
                              "tests/fixtures/file_nested2.yaml",
                              'plain',
                              "tests/fixtures/expected_plain_output.txt"),
                             ("tests/fixtures/file_nested1.yaml",
                              "tests/fixtures/file_nested2.yaml",
                              'json',
                              "tests/fixtures/expected_json_output.txt"),
                             ("tests/fixtures/file_nested1.json",
                              "tests/fixtures/file_nested2.json",
                              'json',
                              "tests/fixtures/expected_json_output.txt"),
                         ])
def test_generate_flat_diff(file_path_1, file_path_2, format_name,
                            expected_output):
    with open(expected_output) as file:
        exp = file.read()
    assert generate_diff(file_path_1, file_path_2, format_name) == exp
