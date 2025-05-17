import sys
import math
import heapq as hq

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
T = 0
while True:
    T += 1
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    acc = [[math.inf for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    heap = []
    hq.heappush(heap, (board[0][0], (0, 0)))
    acc[0][0] = board[0][0]

    while heap:
        value, rowcol = hq.heappop(heap)
        r, c = rowcol[0], rowcol[1]
        if visited[r][c]:
            continue

        for i in range(4):
            next_r, next_c = r + dx[i], c + dy[i]
            if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                next_value = acc[r][c] + board[next_r][next_c]
                if next_value < acc[next_r][next_c]:
                    acc[next_r][next_c] = next_value
                    hq.heappush(heap, (next_value, (next_r, next_c)))
        visited[r][c] = True

    print(f"Problem {T}: {acc[N - 1][N - 1]}")
