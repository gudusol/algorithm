import sys
import math
import heapq as hq
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
maps = defaultdict(list)

for _ in range(M):
    A, B, C = map(int, input().split())
    maps[A].append((B, C))
    maps[B].append((A, C))

distance = [math.inf for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

distance[1] = 0
que = [(0, 1)] # 거리, num
while que:
    cur_dis, cur = hq.heappop(que)
    for next, next_dis in maps[cur]:
        if cur_dis + next_dis < distance[next]:
            distance[next] = cur_dis + next_dis
            hq.heappush(que, (distance[next], next))
    visited[cur] = True

print(distance[N])