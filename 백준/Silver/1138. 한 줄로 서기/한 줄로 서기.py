import sys

input = sys.stdin.readline

N = int(input())
higher = list(map(int, input().split()))
empty_index = [i for i in range(N)]
line = [0 for _ in range(N)]

for idx, h in enumerate(higher):
    index = empty_index[h]
    line[index] = idx + 1
    empty_index.pop(h)
print(*line, sep=" ")
