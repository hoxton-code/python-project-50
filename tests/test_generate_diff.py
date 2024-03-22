from gendiff.diff import generate_diff
import pytest


@pytest.mark.parametrize("file_path_1, file_path_2, expected_output", [
    ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
     "tests/fixtures/expected_plain_output.txt"),
    ("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml",
     "tests/fixtures/expected_plain_output.txt")
])
def test_generate_flat_diff(file_path_1, file_path_2, expected_output):
    with open(expected_output) as file:
        exp = file.read()
    assert generate_diff(file_path_1, file_path_2) == exp
