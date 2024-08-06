import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def get_parent_node(prev, cur):
    global edges, parent_node
    parent_node[cur] = prev

    for node in edges[cur]:
        if node != prev:
            get_parent_node(cur, node)


N = int(input())
edges = {i: [] for i in range(1, N + 1)}
parent_node = {i: -1 for i in range(1, N + 1)}

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

get_parent_node(-1, 1)

for i in range(2, N + 1):
    print(parent_node[i])
