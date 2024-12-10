import numpy as np
import pytest
from day4 import read_input_as_np_array, transform_input_to_rows, transform_input_to_columns, transform_input_to_neg_diagonals, transform_input_to_pos_diagonals, count_xmas_matches

def test_count_xmas_matches_single_word():
    assert count_xmas_matches(['xmas']) == 1
    assert count_xmas_matches(['samx']) == 1
    
def test_count_xmas_matches_multiple_words():
    assert count_xmas_matches(['Xmas xmas','SamX samx']) == 4
    assert count_xmas_matches(['xmas','xmas','xmas']) == 3

def test_count_xmas_matches_overlapping_words():
    assert count_xmas_matches(['samxmas']) == 2
    assert count_xmas_matches(['xmasamx']) == 2
    
def test_count_xmas_matches_no_matches():
    assert count_xmas_matches(['sam','x','s','a','m']) == 0
    
def test_count_xmas_matches_mixed_case():
    assert count_xmas_matches(['bbSnmasXMAShfkdjdfSAMX','jfdkjfdsamx','xma','s']) == 3
    
def test_transform_input_to_rows():
    np_input = np.array([['a','b','c'],['d','e','f']])
    assert transform_input_to_rows(np_input) == ['abc','def']
    
def test_transform_input_to_columns():
    np_input = np.array([['a','b','c'],['d','e','f']])
    assert transform_input_to_columns(np_input) == ['ad','be','cf']
    
def test_transform_input_to_neg_diagonals_square_array():
    np_input = np.array([['a','b','c'],['d','e','f'],['g','h','i']])
    assert transform_input_to_neg_diagonals(np_input) == ['g','dh','aei','bf','c']
    
def test_transform_input_to_neg_diagonals_uneven_array():
    np_input = np.array([['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']])
    assert transform_input_to_neg_diagonals(np_input) == ['j','gk','dhl','aei','bf','c']
    
    np_input = np.array([['a','b','c','d'],['e','f','g','h'],['i','j','k','l']])
    assert transform_input_to_neg_diagonals(np_input) == ['i','ej','afk','bgl','ch','d']
    
def test_transform_input_to_pos_diagonals_square_array():
    np_input = np.array([['a','b','c'],['d','e','f'],['g','h','i']])
    assert transform_input_to_pos_diagonals(np_input) == ['a','db','gec','hf','i']
    
def test_transform_input_to_pos_diagonals_uneven_array():
    np_input = np.array([['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l']])
    assert transform_input_to_pos_diagonals(np_input) == ['a','db','gec','jhf','ki','l']
    
    np_input = np.array([['a','b','c','d'],['e','f','g','h'],['i','j','k','l']])
    assert transform_input_to_pos_diagonals(np_input) == ['a','eb','ifc','jgd','kh','l']
