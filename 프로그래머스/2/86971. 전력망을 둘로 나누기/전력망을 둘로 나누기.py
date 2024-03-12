from collections import deque

# node가 포함된 트리의 노드개수 찾는 함수
def bfs(node, edges, visited):
    q = deque([])
    q.append(node)
    count = 0
    while len(q) > 0:
        cur_node = q.popleft()
        visited[cur_node] = True
        count += 1
        for edge in edges[cur_node]:
            if not visited[edge]:
                q.append(edge)
    return count

def solution(n, wires):
    edges = {i: [] for i in range(1, n + 1)}
    answer = []
    for a, b in wires:
        edges[a].append(b)
        edges[b].append(a)

    for a, b in wires:
        visited = [True] + [False] * (n + 1)
        edges[a].remove(b)
        edges[b].remove(a)

        answer.append(abs(n - (2 * bfs(1, edges, visited))))
        
        edges[a].append(b)
        edges[b].append(a)

    return min(answer)