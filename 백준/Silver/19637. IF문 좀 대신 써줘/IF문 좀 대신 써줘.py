import sys
from bisect import bisect_left as left

input = sys.stdin.readline

N, M = map(int, input().split())

labels = []
ranges = []

for _ in range(N):
    input_str = input().strip().split()
    l, r = input_str[0], int(input_str[1])
    labels.append(l)
    ranges.append(r)

powers = [int(input()) for _ in range(M)]

for p in powers:
    print(labels[left(ranges, p)])
