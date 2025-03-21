import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

city = {i: [] for i in range(1, N + 1)}

for i in range(1, N + 1):
    line = map(int, input().split())
    for j, link in enumerate(line):
        if link == 1:
            city[i].append(j + 1)

plan = list(map(int, input().split()))

linked_city = {i: [] for i in range(1, N + 1)}

for i in range(1, N +1):
    visited = [False] * (N + 1)
    que = deque([i])

    while que:
        cur = que.popleft()
        visited[cur] = True
        linked_city[i].append(cur)
        for c in city[cur]:
            if not visited[c]:
                que.append(c)

for idx in range(len(plan) - 1):
    cur =  plan[idx]
    next = plan[idx + 1]
    if next not in linked_city[cur]:
        print("NO")
        exit()
print("YES")
