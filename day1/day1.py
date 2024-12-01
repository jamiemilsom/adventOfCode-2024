import pandas as pd
from io import StringIO
from typing import Tuple

def read_and_sort_historians_lists(csv_data: str) -> Tuple[list, list]:
    try:
        if '\n' in csv_data or ' ' in csv_data:
            csv_data = StringIO(csv_data)
        df = pd.read_csv(csv_data, header=None)
    except FileNotFoundError:
        raise ValueError(f"Invalid input: {csv_data} is neither a valid file path nor a CSV string.")

    df['list_one'] = df[0].str.split(' ').str[0].astype(int)
    df['list_two'] = df[0].str.split(' ').str[-1].astype(int)

    list_one = sorted(df['list_one'])
    list_two = sorted(df['list_two'])
    return list_one, list_two


def calculate_distance_between_lists(list_one: list, list_two: list) -> int:
    return sum(abs(a - b) for a, b in zip(list_one, list_two))

def compute_total_distance(csv_data: str) -> int:
    list_one, list_two = read_and_sort_historians_lists(csv_data)
    return calculate_distance_between_lists(list_one, list_two)

if __name__ == '__main__':

    print(compute_total_distance('day1/input.csv'))
