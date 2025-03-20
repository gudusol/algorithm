import sys
import math

input = sys.stdin.readline

N = int(input())
values = list(map(int, input().split()))

left = 0
right = N - 1
answer = abs(values[left] + values[right])
answer_idx = [left, right]


while left < right:
    temp = values[left] + values[right]

    if abs(temp) < answer:
        answer = abs(temp)
        answer_idx = [left, right]

    if temp < 0:
        left += 1
    elif temp > 0:
        right -= 1
    else:
        break


print(values[answer_idx[0]], values[answer_idx[1]])
