import sys
from bisect import bisect_right

input = sys.stdin.readline

P = int(input())
for _ in range(P):
    answer = 0
    current_line = []
    input_str = list(map(int, input().split()))
    T = input_str[0]
    line = input_str[1:]

    for height in line:
        idx = bisect_right(current_line, height)
        answer += len(current_line[idx:])
        current_line.insert(idx, height)

    print(f"{T} {answer}")
