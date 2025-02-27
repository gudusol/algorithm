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
    def bfs(cur):
        node_count, edge_count = [1, 0]
        visited[cur] = True
        queue = deque([cur])
        
        while queue:
            node = queue.popleft()
            for next_node in to_edges[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    node_count += 1
                    edge_count += 1
                    queue.append(next_node)
                else:
                    edge_count += 1
        
        return node_count, edge_count
    for node in to_edges[answer[0]]:
        node_count, edge_count = bfs(node)

        if node_count == edge_count:
            answer[1] += 1
        elif node_count == edge_count + 1:
            answer[2] += 1
        elif node_count + 1 == edge_count:
            answer[3] += 1
    
    return answer