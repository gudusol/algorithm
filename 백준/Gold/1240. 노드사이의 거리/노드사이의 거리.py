import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def get_distance(cur, prev, total_distance):
    global end

    if cur == end:
        print(total_distance)
        return True

    for node in edges[cur]:
        num, distance = node
        if num != prev:
            is_find = get_distance(num, cur, total_distance + distance)
            if is_find:
                return True

    return False


N, M = map(int, input().split())
edges = {i: [] for i in range(1, N + 1)}
queries = []

for _ in range(N - 1):
    node1, node2, input_distance = map(int, input().split())
    edges[node1].append((node2, input_distance))
    edges[node2].append((node1, input_distance))

for _ in range(M):
    queries.append(tuple(map(int, input().split())))

for query in queries:
    start, end = query

    get_distance(start, -1, 0)
