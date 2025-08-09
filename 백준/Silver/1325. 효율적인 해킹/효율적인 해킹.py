import sys
from collections import deque

input = sys.stdin.readline
def bfs(s):
    visited = [0 for _ in range(n + 1)]
    visited[s] = True
    queue = deque([s])
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
    return sum(visited)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    com1, com2 = map(int, input().split())
    graph[com2].append(com1)
answer = []
max_v = 0
for i in range(1, n + 1):
    tmp_v = bfs(i)
    if max_v < tmp_v:
        answer = [i]
        max_v = tmp_v
    elif max_v == tmp_v:
        answer.append(i)
print(*answer)
