import csv
import numpy as np
from typing import Tuple


def read_input(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        return np.array([list(row[0]) for row in reader])
    
def get_guard_position(map_arr: np.array) -> Tuple[np.array, np.array]:
    guard_icons = ['^', 'v', '<', '>']
    for icon in guard_icons:
        if icon in map_arr:
            return np.where(map_arr == icon)
    raise ValueError('No guard icon found in map')

def get_guard_direction(map_arr: np.array) -> str:
    guard_icons = ['^', 'v', '<', '>']
    guard_icons_dict = {'^': 'North', 'v': 'South', '<': 'West', '>': 'East'}
    for icon in guard_icons:
        if icon in map_arr:
            return guard_icons_dict[icon]
    raise ValueError('No guard icon found in map')

def get_guard_next_position(map_arr: np.array) -> Tuple[np.array, np.array, bool]:
    guard_position = get_guard_position(map_arr)
    guard_direction = get_guard_direction(map_arr)
    guard_movement = {'North': [1, 0], 'South': [-1, 0], 'West': [0, -1], 'East': [0, 1]}
    
    up_movement = guard_movement[guard_direction][0]
    right_movement = guard_movement[guard_direction][1]
    
    current_row = guard_position[0][0]
    current_col = guard_position[1][0]
    
    is_in_map = True
    
    while True:
        new_row = current_row - up_movement
        new_col = current_col + right_movement
        
        if (new_row < 0 or new_row >= map_arr.shape[0] or 
            new_col < 0 or new_col >= map_arr.shape[1]):
            is_in_map = False
            break
        
        if map_arr[new_row, new_col] == '#':
            break
        
        current_row = new_row
        current_col = new_col
    
    return np.array([current_row]), np.array([current_col]), is_in_map


def update_guard_direction(guard_direction:str) -> str:
    guard_directions = ['North', 'East', 'South', 'West']
    return guard_directions[(guard_directions.index(guard_direction) + 1) % 4]

def draw_crosses(guard_position, guard_next_position, guard_positions):
    up_change = (guard_next_position[0] - guard_position[0])[0]
    right_change = (guard_next_position[1] - guard_position[1])[0]
    
    
    if up_change !=0:
        for i in range(0, up_change, np.sign(up_change)):
            guard_positions[guard_position[0] + i, guard_position[1]] = 'X'
            
    if right_change != 0:
        for i in range(0, right_change, np.sign(right_change)):
            guard_positions[guard_position[0], guard_position[1] + i] = 'X'
    return guard_positions

def get_guard_positions(map_arr: np.array) -> np.array:
    guard_positions = map_arr.copy()
    guard_position = get_guard_position(map_arr)
    guard_direction = get_guard_direction(map_arr)
    guard_next_position = get_guard_next_position(map_arr)
    guard_directions_to_icons = {'North': '^', 'South': 'v', 'West': '<', 'East': '>'}
    
    while guard_next_position[2]:
        guard_positions = draw_crosses(guard_position, guard_next_position, guard_positions)
                
        guard_direction = update_guard_direction(guard_direction)
        guard_positions[guard_next_position[0], guard_next_position[1]] = guard_directions_to_icons[guard_direction]
        guard_position = get_guard_position(guard_positions)

        guard_next_position = get_guard_next_position(guard_positions)
        if not guard_next_position[2]:
            draw_crosses(guard_position, guard_next_position, guard_positions)
            guard_positions[guard_next_position[0], guard_next_position[1]] = 'X'
        

    return guard_positions
    
def get_num_distinct_positions(guard_positions_arr: np.array) -> int:
    return guard_positions_arr.flatten().tolist().count('X')

    
    
if __name__ == '__main__':
        
    map_arr = read_input('day6/input.txt')
    

    print(map_arr)
    guard_position = get_guard_position(map_arr)
    print(guard_position)
    print(guard_position[0], guard_position[1])
    print(map_arr[guard_position[0], guard_position[1]])
    next_guard_position = get_guard_next_position(map_arr)
    print(next_guard_position)
    print(get_guard_positions(map_arr))
    print(get_num_distinct_positions(get_guard_positions(map_arr)))