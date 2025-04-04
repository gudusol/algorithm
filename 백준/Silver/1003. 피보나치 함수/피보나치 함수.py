import sys

input = sys.stdin.readline

fibonacci_arr = [0, 1]

T = int(input())
cases = [int(input()) for _ in range(T)]

for _ in range(max(cases)):
    fibonacci_arr.append(fibonacci_arr[-1] + fibonacci_arr[-2])

for c in cases:
    if c == 0:
        print(1, 0)
    else:
        print(fibonacci_arr[c - 1], fibonacci_arr[c])
