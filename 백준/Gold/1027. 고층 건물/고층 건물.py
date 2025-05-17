import sys

input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))
answer = 0
for idx, h in enumerate(height):
    count = 0
    if idx != 0:
        count += 1
    if idx != N - 1:
        count += 1

    cur_idx = idx - 2
    inclination = (h - height[idx - 1])
    while 0 <= cur_idx:
        cur_inclination = (h - height[cur_idx]) / (idx - cur_idx)
        if cur_inclination < inclination:
            count += 1
            inclination = cur_inclination
        cur_idx -= 1
    
    cur_idx = idx + 2
    if idx < N - 1:
        inclination = (height[idx + 1] - h)
    while cur_idx < N:
        cur_inclination = (height[cur_idx] - h) / (cur_idx - idx)
        if cur_inclination > inclination:
            count += 1
            inclination = cur_inclination
        cur_idx += 1
    answer = max(answer, count)
print(answer)