import csv
import re

def read_entire_input_as_string(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
        return content

def find_mul_statements(input_string):
    """
    Mul statements are of the form:
    mul(a,b)
    where a and b are 1-3 digit numbers
    if there is any deviation from this format, the statement is invalid even just spaces
    """
    mul_statements = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_string)
    return mul_statements


def sum_mul_statements(mul_statements):
    total = 0
    for statement in mul_statements:
        total += int(statement[0]) * int(statement[1])
    return total



if __name__ == '__main__':
    input_string = read_entire_input_as_string('day3/input.txt')
    mul_statements = find_mul_statements(input_string)
    total = sum_mul_statements(mul_statements)
    print('part 1:', total)