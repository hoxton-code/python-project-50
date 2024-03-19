from gendiff.diff import generate_diff
import pytest


@pytest.mark.parametrize("file_path_1, file_path_2, expected_output", [
    ("test/fixtures/file1.json", "test/fixtures/file2.json",
     "test/fixtures/expected_result.txt")
])
def test_generate_diff(file_path_1, file_path_2, expected_output):
    with open(expected_output) as file:
        exp = file.read()
    assert generate_diff(file_path_1, file_path_2) == exp
