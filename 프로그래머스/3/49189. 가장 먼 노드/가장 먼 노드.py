from collections import deque
    
def solution(n, edge):
    nodes = {i: [] for i in range(1, n + 1)}
    for n1, n2 in edge:
        nodes[n1].append(n2)
        nodes[n2].append(n1)
    
    distance = [-1 for _ in range(n + 1)]
    distance[1] = 0
    que = deque([1])

    while que:
        cur = que.popleft()
        for node in nodes[cur]:
            if distance[node] == -1:
                distance[node] = distance[cur] + 1
                que.append(node)
        
    return distance.count(max(distance))