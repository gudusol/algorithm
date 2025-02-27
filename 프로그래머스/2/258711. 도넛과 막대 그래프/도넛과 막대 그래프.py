import sys
sys.setrecursionlimit(10**6)
from collections import deque, defaultdict

def solution(edges):
    answer = [0, 0, 0, 0]
    to_edges = defaultdict(list)
    from_edges = defaultdict(list)
    nodes = set()
    for a, b in edges:
        nodes.add(a)
        nodes.add(b)
        if a in to_edges:
            to_edges[a].append(b)
        else:
            to_edges[a] = [b]
            
        if b in from_edges:
            from_edges[b].append(a)
        else:
            from_edges[b] = [a]
    
    start_nodes = [i for i in nodes]
    start_nodes = list(filter(lambda x: x not in from_edges.keys(), start_nodes))
    
    for n in start_nodes:
        if len(to_edges[n]) >= 2:
            answer[0] = n
            break
    
    visited = [False for _ in range(max(nodes) + 1)]
    def dfs(cur, count):
        count[0] += 1
        count[1] += len(to_edges[cur])
        for node in to_edges[cur]:
            if not visited[node]:
                visited[node] = True
                dfs(node, count)

    for node in to_edges[answer[0]]:
        count = [0, 0]
        visited[node] = True
        
        dfs(node, count)

        if count[0] == count[1]:
            answer[1] += 1
        elif count[0] == count[1] + 1:
            answer[2] += 1
        elif count[0] + 1 == count[1]:
            answer[3] += 1
    
    return answer