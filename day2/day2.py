import csv


def difference_between_levels(lst):
    if len(lst) < 2:
        return []
    
    return [lst[i+1] - lst[i] for i in range(len(lst) - 1)]

def is_list_increasing(lst):
    differences = difference_between_levels(lst)
    
    if len(differences) == 0:
        return False, None
    
    for diff in differences:
        if diff < 1:
            return False, None
        
    return True, differences

def is_list_decreasing(lst):
    differences = difference_between_levels(lst)
    
    if len(differences) == 0:
        return False, None
    
    for diff in differences:
        if diff > -1:
            return False, None
        
    return True, differences

def is_list_safe(lst):
    increasing, differences = is_list_increasing(lst)
    if increasing == False:
        decreasing, differences = is_list_decreasing(lst)
        if decreasing == False:
            return False
    
    for diff in differences:
        if abs(diff) > 3:
            return False
        
    return True

def read_csv_rows_as_numbers(file_path):
    rows = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file, delimiter=' ')
        for row in csv_reader:
            rows.append([int(num) for num in row if num])
    return rows
    
if __name__ == '__main__':
    rows = read_csv_rows_as_numbers('day2/input.txt')
    count = 0
    for row in rows:
        if is_list_safe(row):
            count+=1
            print(row)
            
    print(count)
    
    