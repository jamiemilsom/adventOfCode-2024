import csv
from typing import Tuple

def read_rules_and_page_numbers(file_path: str) -> tuple:
    """
    reads the rules from format X|Y and returns a list of rules in from [[X1, Y1],[X2, Y2],...]
    reads the page numbers from format n1,n2,n3 and returns a list of page numbers in from [[n1, n2, n3],...]
    input file must be in this format
    """
    rules, page_numbers_list = [], []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if '|' in line:
                rules.append(list(map(int, line.split('|'))))
            elif ',' in line:
                page_numbers_list.append(list(map(int, line.split(','))))
    return rules, page_numbers_list


def convert_rules_to_dict(rules: list) -> list:
    """
    converts [[X1,Y1],[X2,Y2],...] to dict{X1:[Y1,Y10,...],X2,[Y2,Y6,...]}
    meaning keys = X1, X2,...
    and values = all Y values for each key
    """
    rules = sorted(rules, key=lambda x: x[0])
    rules_dict = {}
    curr_X = rules[0][0]
    last_X = rules[0][0]
    Y_list = []
    for rule in rules:
        curr_X = rule[0]
        
        if curr_X != last_X:
            rules_dict[last_X] = Y_list
            Y_list = []
            
        Y_list.append(rule[1]) 
        last_X = curr_X 
        
    rules_dict[last_X] = Y_list
    return rules_dict
        

def check_page_number_order(page_numbers: list, rules_dict: dict) -> Tuple[list, bool]:
    """
    checks if the page numbers are in the correct order according to the rules
    returns the correct order of the page numbers, and a boolean value indicating if the page numbers were in the correct order
    """
    correct_order = []
    for page_number in page_numbers:
        try:
            Y_list = rules_dict[page_number] # the numbers that should not be before page_number
        except KeyError:
            Y_list = []
        
        inserted = False

        for i in range(len(correct_order)):

            if correct_order[i] in Y_list:
                correct_order.insert(i, page_number)
                inserted = True
                break
        
        if not inserted:
            correct_order.append(page_number)

    return correct_order, correct_order == page_numbers

            
def update_page_orders(rules_dict, page_numbers_list):
    return [check_page_number_order(page_numbers,rules_dict)[0] for page_numbers in page_numbers_list]

def find_middle_page_number(page_numbers_list):
    return [page_numbers[len(page_numbers) // 2] for page_numbers in page_numbers_list]
    

if __name__ == '__main__':
    rules, page_numbers_list = read_rules_and_page_numbers('day5/input.txt')
    correct_orders = [check_page_number_order(page_numbers, convert_rules_to_dict(rules))[0] for page_numbers in page_numbers_list if check_page_number_order(page_numbers, convert_rules_to_dict(rules))[1]]
    print('part 1:', sum(find_middle_page_number(correct_orders)))
    
    # 5129 is the correct answer