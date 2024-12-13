import pytest
from day5 import read_rules_and_page_numbers, convert_rules_to_dict, check_page_number_order, update_page_orders, find_middle_page_number

@pytest.fixture
def sample_txt_string():
    return """3|4
4|3
2|5
1|3
3|9
3|8

1,2,3,4,5,6,7,8,9,10
10,9,8,7,6,5,4,3,2,1
1,3,5,7,9,2,4,6,8,10"""

@pytest.fixture
def example_txt_string():
    return """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


@pytest.fixture
def sample_csv_file(tmp_path, sample_txt_string):
    file_path = tmp_path / "test_input.txt"
    file_path.write_text(sample_txt_string)
    return file_path

@pytest.fixture
def example_csv_file(tmp_path, example_txt_string):
    file_path = tmp_path / "test_input.txt"
    file_path.write_text(example_txt_string)
    return file_path

def test_read_rules_and_page_numbers(sample_csv_file):
    rules, page_numbers = read_rules_and_page_numbers(sample_csv_file)

    assert rules == [[3, 4], [4, 3], [2, 5], [1, 3], [3, 9], [3, 8]]
    assert page_numbers == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]]

def test_read_rules_and_page_numbers_example(example_csv_file):
    rules, page_numbers = read_rules_and_page_numbers(example_csv_file)

    assert rules == [[47,53],[97,13],[97,61],[97,47],[75,29],[61,13],[75,53],[29,13],[97,29],[53,29],[61,53],[97,53],[61,29],[47,13],[75,47],[97,75],[47,61],[75,61],[47,29],[75,13],[53,13]]
    assert page_numbers == [[75, 47, 61, 53, 29], [97, 61, 53, 29, 13], [75, 29, 13], [75, 97, 47, 61, 53], [61, 13, 29], [97, 13, 75, 29, 47]]

def test_convert_rules_to_dict_presorted():
    rules = [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4], [3, 5], [4, 5], [4, 6], [5, 6], [5, 7], [6, 7], [6, 8], [7, 8], [7, 9], [8, 9], [8, 10], [9, 10]]
    assert convert_rules_to_dict(rules) == {1: [2, 3], 2: [3, 4], 3: [4, 5], 4: [5, 6], 5: [6, 7], 6: [7, 8], 7: [8, 9], 8: [9, 10], 9: [10]}

def test_convert_rules_to_dict_unsorted():
    rules = [[2, 3], [1, 2], [3, 4], [1, 3], [4, 5], [2, 4], [5, 6], [3, 5], [6, 7], [4, 6], [7, 8], [5, 7], [8, 9], [6, 8], [9, 10], [7, 9], [8, 10]]
    assert convert_rules_to_dict(rules) == {1: [2, 3], 2: [3, 4], 3: [4, 5], 4: [5, 6], 5: [6, 7], 6: [7, 8], 7: [8, 9], 8: [9, 10], 9: [10]}
    
def test_convert_rules_to_dict_example():
    rules = [[47,53],[97,13],[97,61],[97,47],[75,29],[61,13],[75,53],[29,13],[97,29],[53,29],[61,53],[97,53],[61,29],[47,13],[75,47],[97,75],[47,61],[75,61],[47,29],[75,13],[53,13]]
    assert convert_rules_to_dict(rules) == {29:[13], 47:[53, 13, 61, 29], 53:[29, 13], 61:[13, 53, 29], 75:[29, 53, 47, 61, 13], 97:[13, 61, 47, 29, 53, 75]}

def test_check_page_number_order_correct_order():
    page_numbers = [1,2,3,4,5,6,7,8,9,10]
    rules = {1: [2], 2: [3], 3: [4], 4: [5], 5: [6], 6: [7], 7: [8], 8: [9], 9: [10]}
    assert check_page_number_order(page_numbers, rules) == ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True)
    
def test_check_page_number_order_incorrect_order():
    page_numbers = [1,2,3,4,5,6,7,8,9,10]
    rules = {2: [1], 3: [2], 4: [3], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8], 10: [9]}
    assert check_page_number_order(page_numbers, rules) == ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], False)
    
def test_check_page_number_order_no_rules():
    page_numbers = [1,2,3,4,5,6,7,8,9,10]
    rules = {}
    assert check_page_number_order(page_numbers, rules) == ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True)
    
def test_check_page_number_order_no_page_numbers():
    page_numbers = []
    rules = {1: [2], 2: [3], 3: [4], 4: [5], 5: [6], 6: [7], 7: [8], 8: [9], 9: [10]}
    assert check_page_number_order(page_numbers, rules) == ([], True)
    
def test_check_page_number_order_example():
    rules = {29:[13], 47:[53, 13, 61, 29], 53:[29, 13], 61:[13, 53, 29], 75:[29, 53, 47, 61, 13], 97:[13, 61, 47, 29, 53, 75]}
    
    page_numbers = [75, 47, 61, 53, 29]
    assert check_page_number_order(page_numbers, rules) == (page_numbers, True)
    
    page_numbers = [97, 61, 53, 29, 13]
    assert check_page_number_order(page_numbers, rules) == (page_numbers, True)
    
    page_numbers = [75, 29, 13]
    assert check_page_number_order(page_numbers, rules) == (page_numbers, True)
    
    page_numbers = [75, 97, 47, 61, 53]
    assert check_page_number_order(page_numbers, rules) == ([97, 75, 47, 61, 53], False)
    
    page_numbers = [61, 13, 29]
    assert check_page_number_order(page_numbers, rules) == ([61, 29, 13], False)
    
    page_numbers = [97, 13, 75, 29, 47]
    assert check_page_number_order(page_numbers, rules) == ([97, 75, 47, 29, 13], False)

def test_update_page_orders():
    page_numbers_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]]
    rules_dict = {1:[2], 2:[3], 3:[4], 4:[5], 5:[6], 6:[7], 7:[8], 8:[9], 9:[10]}
    assert update_page_orders(rules_dict, page_numbers_list) == [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    
def test_find_middle_page_number():
    page_numbers_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 9, 8, 7, 6, 5, 4, 3, 2], [3, 5, 7, 9, 2, 4, 6, 8, 10]]
    assert find_middle_page_number(page_numbers_list) == [5, 6, 2]
    