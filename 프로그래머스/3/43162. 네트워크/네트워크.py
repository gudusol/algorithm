from collections import deque

def bfs(v, computers):
    visited = []
    que = deque([v])
    
    while que:
        cur = que.popleft()
        visited.append(cur)
        for idx, val in enumerate(computers[cur]):
            if cur != idx:
                if idx not in visited and val == 1:
                    que.append(idx)
            
    return visited

def solution(n, computers):
    visited = set()
    count = 0
    for i in range(n):
        if i not in visited:
            visited.update(bfs(i, computers))
            count += 1
        if len(visited) == n:
            return count
    return