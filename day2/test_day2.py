import pytest
from day2 import is_list_increasing, is_list_decreasing, difference_between_levels, is_list_safe, is_list_safe_with_one_removed

"""
pt 1
The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

pt 2
Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
"""

def test_large_increasing_list():
    test_lst = [0, 10, 20, 40, 50]
    assert is_list_increasing(test_lst) == (True, [10, 10, 20, 10])
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False
    assert is_list_safe_with_one_removed(test_lst) == False

def test_large_decreasing_list():
    test_lst = [50, 40, 30, 20, 10]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (True, [-10, -10, -10, -10])
    assert is_list_safe(test_lst) == False
    assert is_list_safe_with_one_removed(test_lst) == False

def test_small_increasing_list():
    test_lst = [1, 2, 3, 4, 5]
    assert is_list_increasing(test_lst) == (True, [1, 1, 1, 1])
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == True
    assert is_list_safe_with_one_removed(test_lst) == True

def test_small_decreasing_list():
    test_lst = [5, 4, 3, 2, 1]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (True, [-1, -1, -1, -1])
    assert is_list_safe(test_lst) == True
    assert is_list_safe_with_one_removed(test_lst) == True

def test_mixed_list():
    test_lst = [1, 2, 5, 4, 3]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False
    assert is_list_safe_with_one_removed(test_lst) == False

def test_same_level_list():
    test_lst = [3, 3, 3, 3, 3]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False
    assert is_list_safe_with_one_removed(test_lst) == False
    

def test_empty_list():
    test_lst = []
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False
    assert is_list_safe_with_one_removed(test_lst) == False

def test_single_level_list():
    test_lst = [1]
    assert is_list_increasing(test_lst) == (False, None)
    assert is_list_decreasing(test_lst) == (False, None)
    assert is_list_safe(test_lst) == False
    assert is_list_safe_with_one_removed(test_lst) == False

def test_limit_list():
    test_lst_1 = [1, 2, 3]
    assert is_list_increasing(test_lst_1) == (True, [1, 1])
    assert is_list_decreasing(test_lst_1) == (False, None)
    assert is_list_safe(test_lst_1) == True
    assert is_list_safe_with_one_removed(test_lst_1) == True

    test_lst_2 = [1, 4, 7]
    assert is_list_increasing(test_lst_2) == (True, [3, 3])
    assert is_list_decreasing(test_lst_2) == (False, None)
    assert is_list_safe(test_lst_2) == True
    assert is_list_safe_with_one_removed(test_lst_2) == True
    
def test_one_removed_cases():
    test_lst_1 = [7, 6, 4, 2, 1]
    assert is_list_safe_with_one_removed(test_lst_1) == True

    test_lst_2 = [1, 2, 7, 8, 9]
    assert is_list_safe_with_one_removed(test_lst_2) == False

    test_lst_3 = [9, 7, 6, 2, 1]
    assert is_list_safe_with_one_removed(test_lst_3) == False

    test_lst_4 = [1, 3, 2, 4, 5]
    assert is_list_safe_with_one_removed(test_lst_4) == True

    test_lst_5 = [8, 6, 4, 4, 1]
    assert is_list_safe_with_one_removed(test_lst_5) == True

    test_lst_6 = [1, 3, 6, 7, 9]
    assert is_list_safe_with_one_removed(test_lst_6) == True
    
