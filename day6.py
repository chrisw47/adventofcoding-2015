import re
import numpy as np

instructions = open('day6.txt', 'r').read().splitlines()

# Part 1

def turn_on(grid: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    grid[x1 : x2+1, y1 : y2+1] = 1
    return grid

def turn_off(grid: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    grid[x1 : x2+1, y1 : y2+1] = 0
    return grid

def toggle(grid: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    switch = {0: 1, 1: 0}
    grid[x1 : x2+1, y1 : y2+1] = np.vectorize(switch.get)(grid[x1 : x2+1, y1 : y2+1])
    return grid

grid = np.zeros((1000, 1000))

for instruction in instructions:

    idx = re.search(r'(\d)', instruction).start()
    coords = [int(coord) for coord in re.findall(r'(\d+)', instruction)]

    if idx == 7:
        toggle(grid, coords[0], coords[1], coords[2], coords[3])
    elif idx == 8:
        turn_on(grid, coords[0], coords[1], coords[2], coords[3])
    elif idx == 9:
        turn_off(grid, coords[0], coords[1], coords[2], coords[3])


print(f'Total brightness: {np.sum(grid)}.')

# Part 2:

def inc_bright(grid: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    grid[x1 : x2+1, y1 : y2+1] += 1
    return grid

def dec_bright(grid: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    s = grid[x1 : x2+1, y1 : y2+1]
    grid[x1 : x2+1, y1 : y2+1] = np.where(s > 0, s-1, s)
    return grid

def tog_2(grid: np.ndarray, x1: int, y1: int, x2: int, y2: int):
    grid[x1 : x2+1, y1 : y2+1] += 2
    return grid

grid = np.zeros((1000, 1000))

for instruction in instructions:

    idx = re.search(r'(\d)', instruction).start()
    coords = [int(coord) for coord in re.findall(r'(\d+)', instruction)]

    if idx == 7:
        tog_2(grid, coords[0], coords[1], coords[2], coords[3])
    elif idx == 8:
        inc_bright(grid, coords[0], coords[1], coords[2], coords[3])
    elif idx == 9:
        dec_bright(grid, coords[0], coords[1], coords[2], coords[3])

print(f'Total brightness: {np.sum(grid)}.')