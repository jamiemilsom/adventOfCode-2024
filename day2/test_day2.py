import pytest
from day2 import is_list_increasing, is_list_decreasing, difference_between_levels, is_list_safe

"""
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
"""

def test_large_increasing_list():
    test_lst = [0, 10, 20, 40, 50]
    assert is_list_increasing(test_lst) == (True, [10, 10, 20, 10])
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False

def test_large_decreasing_list():
    test_lst = [50, 40, 30, 20, 10]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (True, [-10, -10, -10, -10])
    assert is_list_safe(test_lst) == False

def test_small_increasing_list():
    test_lst = [1, 2, 3, 4, 5]
    assert is_list_increasing(test_lst) == (True, [1, 1, 1, 1])
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == True

def test_small_decreasing_list():
    test_lst = [5, 4, 3, 2, 1]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (True, [-1, -1, -1, -1])
    assert is_list_safe(test_lst) == True

def test_mixed_list():
    test_lst = [1, 2, 5, 4, 3]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False

def test_same_level_list():
    test_lst = [3, 3, 3, 3, 3]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False

def test_empty_list():
    test_lst = []
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False

def test_single_level_list():
    test_lst = [1]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False

def test_limit_list():
    test_lst_1 = [1, 2, 3]
    assert is_list_increasing(test_lst_1) == (True, [1, 1])
    assert is_list_decreasing(test_lst_1) == (False, None)
    assert is_list_safe(test_lst_1) == True

    test_lst_2 = [1, 4, 7]
    assert is_list_increasing(test_lst_2) == (True, [3, 3])
    assert is_list_decreasing(test_lst_2) == (False, None)
    assert is_list_safe(test_lst_2) == True
