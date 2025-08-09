import sys
import math

input = sys.stdin.readline


N, K = map(int, input().split())
dis = []
for _ in range(N):
    dis.append(list(map(int, input().split())))

for cur in range(N):
    for start in range(N):
        if start == cur:
            continue
        for end in range(N):
            if end == cur:
                continue
            dis[start][end] = min(dis[start][end], dis[start][cur] + dis[cur][end])

visited = [False for _ in range(N)]
answer = math.inf
def dfs(cur, acc):
    global answer
    if visited.count(False) == 0:
        answer = min(answer, acc)
        return
    for next_idx, next_dis in enumerate(dis[cur]):
        if not visited[next_idx]:
            visited[next_idx] = True
            dfs(next_idx, acc + next_dis)
            visited[next_idx] = False

visited[K] = True
dfs(K, 0)

print(answer)