import pandas as pd
from io import StringIO
import pytest
from day1 import read_and_sort_historians_lists, calculate_distance_between_lists, compute_total_distance

@pytest.fixture
def sample_csv_string():
    return """3 4
4 3
2 5
1 3
3 9
3 3"""

@pytest.fixture
def sample_csv_file(tmp_path, sample_csv_string):
    file_path = tmp_path / "test_input.csv"
    file_path.write_text(sample_csv_string)
    return file_path

def test_read_and_sort_historians_lists_from_string(sample_csv_string):
    list_one, list_two = read_and_sort_historians_lists(sample_csv_string)
    assert list_one == [1, 2, 3, 3, 3, 4]
    assert list_two == [3, 3, 3, 4, 5, 9]

def test_read_and_sort_historians_lists_from_file(sample_csv_file):
    list_one, list_two = read_and_sort_historians_lists(str(sample_csv_file))
    assert list_one == [1, 2, 3, 3, 3, 4]
    assert list_two == [3, 3, 3, 4, 5, 9]

def test_calculate_distance_between_lists():
    list_one = [1, 2, 3, 3, 3, 4]
    list_two = [3, 3, 3, 4, 5, 9]
    assert calculate_distance_between_lists(list_one, list_two) == 11

def test_compute_total_distance_from_string(sample_csv_string):
    total_distance = compute_total_distance(sample_csv_string)
    assert total_distance == 11

def test_compute_total_distance_from_file(sample_csv_file):
    total_distance = compute_total_distance(str(sample_csv_file))
    assert total_distance == 11

def test_empty_input():
    empty_csv = ""
    with pytest.raises(ValueError, match=f"Invalid input: {empty_csv} is neither a valid file path nor a CSV string."):
        read_and_sort_historians_lists(empty_csv)

def test_single_row_input():
    single_row_csv = "10 20"
    list_one, list_two = read_and_sort_historians_lists(single_row_csv)
    assert list_one == [10]
    assert list_two == [20]
    assert calculate_distance_between_lists(list_one, list_two) == 10
    assert compute_total_distance(single_row_csv) == 10

