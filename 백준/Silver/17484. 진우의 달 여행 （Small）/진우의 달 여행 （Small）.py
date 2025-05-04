import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
answer = math.inf


def dfs(i, j, total, prev):
    global answer
    total += board[i][j]
    if i == N - 1:
        answer = min(answer, total)
        return

    if j - 1 >= 0 and prev != 1:
        dfs(i + 1, j - 1, total, 1)
    if prev != 2:
        dfs(i + 1, j, total, 2)
    if j + 1 < M and prev != 3:
        dfs(i + 1, j + 1, total, 3)


for idx, val in enumerate(board[0]):
    dfs(0, idx, 0, 0)

print(answer)
