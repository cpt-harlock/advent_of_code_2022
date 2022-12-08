#!/usr/bin/python3

import argparse
import numpy as np

def is_visible_from_right(row_index, col_index, row_size, col_size, grid):
    if col_index == col_size-1:
        return True
    ret = True
    value = grid[row_index][col_index]
    for i in range(col_index+1, col_size):
        if grid[row_index][i] >= value:
            ret = False
            break
    return ret

def is_visible_from_left(row_index, col_index, row_size, col_size, grid):
    if col_index == 0:
        return True
    ret = True
    value = grid[row_index][col_index]
    for i in range(0, col_index):
        if grid[row_index][i] >= value:
            ret = False
            break
    return ret

def is_visible_from_top(row_index, col_index, row_size, col_size, grid):
    if row_index == 0:
        return True
    ret = True
    value = grid[row_index][col_index]
    for i in range(0, row_index):
        if grid[i][col_index] >= value:
            ret = False
            break
    return ret

def is_visible_from_below(row_index, col_index, row_size, col_size, grid):
    if row_index == row_size-1:
        return True
    ret = True
    value = grid[row_index][col_index]
    for i in range(row_index+1, row_size):
        if grid[i][col_index] >= value:
            ret = False
            break
    return ret

def is_visible(row_index, col_index, row_size, col_size, grid):
    return is_visible_from_below(row_index, col_index, row_size, col_size, grid) or is_visible_from_top(row_index, col_index, row_size, col_size, grid) or is_visible_from_right(row_index, col_index, row_size, col_size, grid) or is_visible_from_left(row_index, col_index, row_size, col_size, grid)

def scenic_score_right(row_index, col_index, row_size, col_size, grid):
    if col_index == col_size-1:
        return 0
    ret = 0
    value = grid[row_index][col_index]
    for i in range(col_index+1, col_size):
        ret += 1
        if grid[row_index][i] >= value:
            break
    return ret

def scenic_score_left(row_index, col_index, row_size, col_size, grid):
    if col_index == 0:
        return 0 
    ret = 0
    value = grid[row_index][col_index]
    for i in reversed(range(0, col_index)):
        ret += 1
        if grid[row_index][i] >= value:
            break
    return ret

def scenic_score_top(row_index, col_index, row_size, col_size, grid):
    if row_index == 0:
        return 0
    ret = 0
    value = grid[row_index][col_index]
    for i in reversed(range(0, row_index)):
        ret += 1
        if grid[i][col_index] >= value:
            break
    return ret

def scenic_score_below(row_index, col_index, row_size, col_size, grid):
    if row_index == row_size-1:
        return 0
    ret = 0
    value = grid[row_index][col_index]
    for i in range(row_index+1, row_size):
        ret += 1
        if grid[i][col_index] >= value:
            break
    return ret

def scenic_score(row_index, col_index, row_size, col_size, grid):
    return scenic_score_below(row_index, col_index, row_size, col_size, grid) * scenic_score_top(row_index, col_index, row_size, col_size, grid) * scenic_score_right(row_index, col_index, row_size, col_size, grid) * scenic_score_left(row_index, col_index, row_size, col_size, grid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=str)
    args = parser.parse_args()
    input_file = args.input

    grid = []
    with open(input_file) as f:
        for line in f.readlines():
            row = []
            for c in line.strip('\n'):
                row.append(int(c))
            grid.append(row)

    visible_count = 0
    row_size = len(grid)
    col_size = len(grid[0])
    for i in range(row_size):
        for j in range(col_size):
            if is_visible(i, j, row_size, col_size, grid):
                visible_count += 1
    print("First half answer:",visible_count)

    max_scenic_score = 0
    max_i = 0
    max_j = 0
    for i in range(row_size):
        for j in range(col_size):
            if scenic_score(i, j, row_size, col_size, grid) > max_scenic_score:
                max_scenic_score = scenic_score(i, j, row_size, col_size, grid)
    print("Second half answer:",max_scenic_score)

