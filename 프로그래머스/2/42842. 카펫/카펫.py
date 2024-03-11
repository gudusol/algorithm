from math import floor

def calculate_brown(row, col):
    return (2 * row) + (2 * col) + 4

def solution(brown, yellow):
    for col in range(1, floor(yellow ** 0.5) + 1):
        if yellow % col == 0:
            row = yellow // col
            brown_num = calculate_brown(row, col)
            if brown == brown_num:
                return [row + 2, col + 2]
