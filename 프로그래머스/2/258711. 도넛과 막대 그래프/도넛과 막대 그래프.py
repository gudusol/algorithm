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
    for node in to_edges[answer[0]]:
        visited[node] = True
        queue = deque([node])
        is_break = False
        while queue:
            cur = queue.popleft()
            
            if len(to_edges[cur]) == 2:
                answer[3] += 1
                is_break = True
                break
            
            if (len(to_edges[cur]) == 0) or (len(from_edges[cur]) == 0):
                answer[2] += 1
                is_break = True
                break
            
            for next_node in to_edges[cur]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
        if not is_break:
            answer[1] += 1
    
    return answer