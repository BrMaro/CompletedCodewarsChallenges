# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python


def find_element_index_2d(array, target):
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == target:
                return i, j
    return None  # Return None if the element is not found


def get_pins(observed):
    keypad = [['1', '2', '3'],
              ['4', '5', '6'],
              ['7', '8', '9'],
              ['-', '0', '-']]

    neighbors = {}
    for i, row in enumerate(keypad):
        for j, key in enumerate(row):
            if key == '-' or key == '':  # Skip invalid keys
                continue
            possible_keys = [key]  # Include the key itself
            if i > 0 and keypad[i - 1][j] != '-':  # Top neighbor
                possible_keys.append(keypad[i - 1][j])
            if i < 3 and keypad[i + 1][j] != '-':  # Bottom neighbor
                possible_keys.append(keypad[i + 1][j])
            if j > 0 and keypad[i][j - 1] != '-':  # Left neighbor
                possible_keys.append(keypad[i][j - 1])
            if j < 2 and keypad[i][j + 1] != '-':  # Right neighbor
                possible_keys.append(keypad[i][j + 1])
            neighbors[key] = possible_keys

    # generate all combinations recursively
    def generate_combinations(current_combination, index):
        if index == len(observed):
            combinations.append(current_combination)
            return
        for neighbor in neighbors[observed[index]]:
            generate_combinations(current_combination + neighbor, index + 1)

    combinations = []
    generate_combinations("", 0)

    print(combinations)
    return combinations


## MOST OPTIMAL SOLN
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')


def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
