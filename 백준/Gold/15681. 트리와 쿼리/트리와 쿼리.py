import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def count_child(parent):
    global queue, edges, child_count
    if len(queue) == 0:
        return

    cur = queue.popleft()
    count = 1
    for node in edges[cur]:
        if node != parent:
            queue.append(node)
            count += count_child(cur)
    child_count[cur] += count
    return child_count[cur]


N, R, Q = map(int, input().split())
edges = {i: [] for i in range(1, N + 1)}
queries = []
for _ in range(N - 1):
    U, V = map(int, input().split())
    edges[U].append(V)
    edges[V].append(U)

for _ in range(Q):
    queries.append(int(input()))

queue = deque([R])
child_count = {i: 0 for i in range(1, N + 1)}

count_child(-1)

for query in queries:
    print(child_count[query])
