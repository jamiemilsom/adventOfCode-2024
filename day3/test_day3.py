import pytest
from day3 import find_mul_statements, sum_mul_statements

def test_find_mul_statements_valid():
    test_string = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    expected = [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    assert find_mul_statements(test_string) == expected

def test_find_mul_statements_no_matches():
    test_string = 'no_mul_here(1,2)!@#$random_text'
    expected = []
    assert find_mul_statements(test_string) == expected

def test_find_mul_statements_partial_matches():
    test_string = 'mul(12,3)mul(4*,5), mul(1 ,2), mul()'
    expected = [('12', '3')]
    assert find_mul_statements(test_string) == expected

def test_find_mul_statements_large_numbers():
    test_string = 'mul(1234,56)mul(78,90123)mul(99,88)'
    expected = [('99', '88')]
    assert find_mul_statements(test_string) == expected

def test_sum_mul_statements_valid():
    test_statements = [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]
    expected = 2 * 4 + 5 * 5 + 11 * 8 + 8 * 5
    assert sum_mul_statements(test_statements) == expected

def test_sum_mul_statements_empty():
    test_statements = []
    expected = 0
    assert sum_mul_statements(test_statements) == expected

def test_sum_mul_statements_large_numbers():
    test_statements = [('999', '999'), ('123', '456')]
    expected = 999 * 999 + 123 * 456
    assert sum_mul_statements(test_statements) == expected
