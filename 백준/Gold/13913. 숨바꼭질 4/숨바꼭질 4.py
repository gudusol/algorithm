import sys
import math
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

if N == K:
    print(0)
    print(N)
    exit()

MAX_LENGTH = 100001

arr = [math.inf] * MAX_LENGTH
visited = [-1] * MAX_LENGTH

arr[N] = 0
visited[N] = N

que = deque([N])

answer_way = []
path = []
while que:
    cur = que.popleft()
    if cur == K:
        cur_path = cur
        while cur_path != N:
            path.append(cur_path)
            cur_path = visited[cur_path]
        path.append(N)
        break

    if cur * 2 < MAX_LENGTH and visited[cur * 2] == -1:
        que.append(cur * 2)
        arr[cur * 2] = arr[cur] + 1
        visited[cur * 2] = cur

    if cur + 1 < MAX_LENGTH and visited[cur + 1] == -1:
        que.append(cur + 1)
        arr[cur + 1] = arr[cur] + 1
        visited[cur + 1] = cur
    if cur - 1 >= 0 and visited[cur - 1] == -1:
        que.append(cur - 1)
        arr[cur - 1] = arr[cur] + 1
        visited[cur - 1] = cur


print(arr[K])
print(" ".join(map(str, reversed(path))))
