import sys
import math
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

MAX_LENGTH = 100001

arr = [math.inf] * MAX_LENGTH
visited = [False] * MAX_LENGTH

arr[N] = 0
visited[N] = True

que = deque([N])
while que:
    cur = que.popleft()

    if cur * 2 < MAX_LENGTH and not visited[cur * 2]:
        que.append(cur * 2)
        arr[cur * 2] = arr[cur] + 1
        visited[cur * 2] = True

    if cur + 1 < MAX_LENGTH and not visited[cur + 1]:
        que.append(cur + 1)
        arr[cur + 1] = arr[cur] + 1
        visited[cur + 1] = True

    if cur - 1 >= 0 and not visited[cur - 1]:
        que.append(cur - 1)
        arr[cur - 1] = arr[cur] + 1
        visited[cur - 1] = True

print(arr[K])
