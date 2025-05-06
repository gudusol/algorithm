import sys

input = sys.stdin.readline


def left_right_length(balls, color):
    left = 0
    right = 0

    for b in balls:
        if b == color:
            left += 1
        else:
            break

    for b in balls[::-1]:
        if b == color:
            right += 1
        else:
            break
    return left, right


N = int(input())
balls = input().strip()

blue = balls.count("B")
red = balls.count("R")

answer = []

# blue
left, right = left_right_length(balls, 'B')
answer.append(blue - max(left, right))

# red
left, right = left_right_length(balls, 'R')
answer.append(red - max(left, right))

print(min(answer))
