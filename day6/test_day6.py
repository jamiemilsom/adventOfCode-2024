import pytest
import numpy as np
from day6 import read_input, get_guard_position, get_guard_direction, update_guard_direction, get_guard_next_position, get_guard_positions, get_num_distinct_positions

@pytest.fixture
def sample_txt_string():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

@pytest.fixture
def sample_txt_file(tmp_path, sample_txt_string):
    file_path = tmp_path / "test_input.txt"
    file_path.write_text(sample_txt_string)
    return file_path

test_map_arr = np.array([
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.']
])


test_guard_positions_arr = np.array([
    ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'X', 'X', 'X', 'X', 'X', '#'],
    ['.', '.', '.', '.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', '#', '.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', 'X', 'X', 'X', 'X', 'X', '#', 'X', '.'],
    ['.', '.', 'X', '.', 'X', '.', 'X', '.', 'X', '.'],
    ['.', '#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.'],
    ['.', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.'],
    ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', 'X', '.', '.']
])




def test_read_input(sample_txt_file):
    np.testing.assert_array_equal(read_input(sample_txt_file), test_map_arr)
    
def test_get_guard_position():
    test_map_pos_arr = test_map_arr.copy()
    assert get_guard_position(test_map_pos_arr) == (np.array([6]), np.array([4]))
    test_map_pos_arr[6, 4] = '.'
    test_map_pos_arr[2, 6] = '<'
    assert get_guard_position(test_map_pos_arr) == (np.array([2]), np.array([6]))
    test_map_pos_arr[2, 6] = '.'
    test_map_pos_arr[7, 1] = '>'
    assert get_guard_position(test_map_pos_arr) == (np.array([7]), np.array([1]))
    test_map_pos_arr[7, 1] = '.'
    test_map_pos_arr[0, 4] = 'v'
    assert get_guard_position(test_map_pos_arr) == (np.array([0]), np.array([4]))
    
def test_get_guard_direction():
    test_map_dir_arr = test_map_arr.copy()
    assert get_guard_direction(test_map_dir_arr) == 'North'
    test_map_dir_arr[6, 4] = 'v'
    assert get_guard_direction(test_map_dir_arr) == 'South'
    test_map_dir_arr[6, 4] = '<'
    assert get_guard_direction(test_map_dir_arr) == 'West'
    test_map_dir_arr[6, 4] = '>'
    assert get_guard_direction(test_map_dir_arr) == 'East'
    
def test_update_guard_direction():
    guard_position = 'North'
    assert update_guard_direction(guard_position) == 'East'
    guard_position = 'East'
    assert update_guard_direction(guard_position) == 'South'
    guard_position = 'South'
    assert update_guard_direction(guard_position) == 'West'
    guard_position = 'West'
    assert update_guard_direction(guard_position) == 'North'
    
def test_get_guard_next_position():
    test_map_next_arr = test_map_arr.copy()
    assert get_guard_next_position(test_map_next_arr)[0] == np.array([1])
    assert get_guard_next_position(test_map_next_arr)[1] == np.array([4])
    assert get_guard_next_position(test_map_next_arr)[2] == True
    test_map_next_arr[1, 4] = '>'
    test_map_next_arr[6, 4] = '.'

    assert get_guard_next_position(test_map_next_arr)[0] == np.array([1])
    assert get_guard_next_position(test_map_next_arr)[1] == np.array([8])
    assert get_guard_next_position(test_map_next_arr)[2] == True
    test_map_next_arr[1, 8] = 'v'
    test_map_next_arr[1, 4] = '.'

    assert get_guard_next_position(test_map_next_arr)[0] == np.array([6])
    assert get_guard_next_position(test_map_next_arr)[1] == np.array([8])
    assert get_guard_next_position(test_map_next_arr)[2] == True
    test_map_next_arr[1, 8] = '.'
    test_map_next_arr[3, 1] = '^'

    assert get_guard_next_position(test_map_next_arr)[0] == np.array([0])
    assert get_guard_next_position(test_map_next_arr)[1] == np.array([1])
    assert get_guard_next_position(test_map_next_arr)[2] == False
    test_map_next_arr[0, 2] = '<'
    test_map_next_arr[3, 1] = '.'

    assert get_guard_next_position(test_map_next_arr)[0] == np.array([0])
    assert get_guard_next_position(test_map_next_arr)[1] == np.array([0])
    assert get_guard_next_position(test_map_next_arr)[2] == False
    test_map_next_arr[7, 7] = 'v'
    test_map_next_arr[0, 2] = '.'

    assert get_guard_next_position(test_map_next_arr)[0] == np.array([9])
    assert get_guard_next_position(test_map_next_arr)[1] == np.array([7])
    assert get_guard_next_position(test_map_next_arr)[2] == False
    
    
    

def test_get_guard_positions():

    np.testing.assert_array_equal(get_guard_positions(test_map_arr), test_guard_positions_arr)
    
def test_get_num_distinct_positions():
    assert get_num_distinct_positions(test_guard_positions_arr) == 41
    
