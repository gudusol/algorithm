import sys
import math
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [0] * 101
visited = [False] * 101

portal = {}

for _ in range(N + M):
    start, end = map(int, input().split())
    portal[start] = end

board[1] = 0
que = deque([1])

while que:
    cur = que.popleft()
    if cur == 100:
        break

    for dice in range(1, 7):
        next = cur + dice
        if next <= 100 and not visited[next]:

            if next in portal:
                next = portal[next]

            if not visited[next]:
                visited[next] = True
                que.append(next)
                board[next] = board[cur] + 1

print(board[100])
