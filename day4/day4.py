import numpy as np

def read_input_as_np_array(file_path):
    with open(file_path, 'r') as file:
        return np.array([[letter for letter in line] for line in file])
    
def transform_input_to_rows(np_input):
    return [''.join(row) for row in np_input]

def transform_input_to_columns(np_input):
    return [''.join(column) for column in np_input.T]

def transform_input_to_neg_diagonals(np_input):
    neg_diagonals = [''.join(np.diagonal(np_input, offset)) for offset in range(-np_input.shape[0]+1, np_input.shape[1])]
    return [''.join(diagonal) for diagonal in neg_diagonals]

def transform_input_to_pos_diagonals(np_input):
    return transform_input_to_neg_diagonals(np.flip(np_input,axis=0))

def count_xmas_matches(list_of_strings):
    count = 0
    for string in list_of_strings:
        count += string.lower().count('xmas') + string.lower().count('samx')
    return count
    
def count_all_xmas_matches(np_input):
    rows = transform_input_to_rows(np_input)
    columns = transform_input_to_columns(np_input)
    neg_diagonals = transform_input_to_neg_diagonals(np_input)
    pos_diagonals = transform_input_to_pos_diagonals(np_input)
    
    return count_xmas_matches(rows) + count_xmas_matches(columns) + count_xmas_matches(neg_diagonals) + count_xmas_matches(pos_diagonals)


def transform_input_to_cross(np_input):
    """
    looping through in the form
    a_b
    _c_
    d_e
    """
    cross_inputs = []
    for i in range(np_input.shape[0]-2):
        for j in range(np_input.shape[1]-2):
        
            a = np_input[i,j].lower()
            b = np_input[i,j+2].lower()
            c = np_input[i+1,j+1].lower()
            d = np_input[i+2,j].lower()
            e = np_input[i+2,j+2].lower()
            cross_inputs.append([a,b,c,d,e]) 
            
    return cross_inputs
           
           
def count_xmas_cross_matches(cross_inputs):
    count = 0
    for cross_values in cross_inputs:
        if cross_values == ['m','s','a','m','s'] or cross_values == ['m','m','a','s','s'] or cross_values == ['s','m','a','s','m'] or cross_values == ['s','s','a','m','m']:
            count += 1
            
    return count
    
    
if __name__ == '__main__':
    input_np = read_input_as_np_array('day4/input.txt')
    print('part 1:', count_all_xmas_matches(input_np))
    
    print('part 2:', count_xmas_cross_matches(transform_input_to_cross(input_np)))

        

    