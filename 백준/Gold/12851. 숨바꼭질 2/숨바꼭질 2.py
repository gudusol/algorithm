import sys
import math
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

MAX_LENGTH = 100001

arr = [math.inf] * MAX_LENGTH
visited = [False] * MAX_LENGTH

arr[N] = 0

que = deque([N])

count = 0
while que:
    cur = que.popleft()
    if cur == K:
        count += 1

    if cur * 2 < MAX_LENGTH and arr[cur * 2] >= arr[cur] + 1:
        que.append(cur * 2)
        arr[cur * 2] = arr[cur] + 1

    if cur + 1 < MAX_LENGTH and arr[cur + 1] >= arr[cur] + 1:
        que.append(cur + 1)
        arr[cur + 1] = arr[cur] + 1

    if cur - 1 >= 0 and arr[cur - 1] >= arr[cur] + 1:
        que.append(cur - 1)
        arr[cur - 1] = arr[cur] + 1

print(arr[K])
print(count)
