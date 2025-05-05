import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
pillar = [list(map(int, input().split())) for _ in range(N)]
pillar.sort()
pillar = deque(pillar)
pillar_height = []
for p in pillar:
    pillar_height.append(p[1])

max_height = max(pillar_height)

max_idx = []
for idx, p in pillar:
    if p == max_height:
        max_idx.append(idx)

left_max = max_idx[0]
right_max = max_idx[-1]

answer = 0

# 최고점 기준 왼쪽
cur = pillar[0]
while pillar[0][0] < left_max:
    next = pillar.popleft()

    if next[1] > cur[1]:
        answer += (next[0] - cur[0]) * cur[1]
        cur = next
answer += (pillar[0][0] - cur[0]) * cur[1]

# 최고점 영역
answer += (right_max - left_max + 1) * max_height

# 최고점 기준 오른쪽
cur = pillar[-1]
while pillar[-1][0] > right_max:
    next = pillar.pop()

    if next[1] > cur[1]:
        answer += (cur[0] - next[0]) * cur[1]
        cur = next

answer += (cur[0] - pillar[-1][0]) * cur[1]
print(answer)
