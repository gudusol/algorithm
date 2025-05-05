import sys
import math

input = sys.stdin.readline

N = int(input())
numbers = []
min_number = math.inf
len_numbers = 0
for _ in range(N):
    for num in list(map(int, input().split())):
        if len_numbers < N:
            numbers.append(num)
            len_numbers += 1
            if num < min_number:
                min_number = num
        else:
            if num > min_number:
                numbers.sort(reverse=True)
                numbers.pop()
                min_number = min(num, numbers[-1])
                numbers.append(num)

print(sorted(numbers, reverse=True)[N - 1])


