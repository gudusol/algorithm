import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

target_x, target_y = 0, 0
for i, row in enumerate(board):
    for j, value in enumerate(row):
        if value == 2:
            target_x, target_y = i, j
            break

visited[target_x][target_y] = True
que = deque([[target_x, target_y]])


board[target_x][target_y] = 0
while que:
    cur_x, cur_y = que.popleft()
    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if not visited[next_x][next_y] and board[next_x][next_y] != 0:
                visited[next_x][next_y] = True
                board[next_x][next_y] = board[cur_x][cur_y] + 1
                que.append([next_x, next_y])

for i, row in enumerate(board):
    for j, value in enumerate(row):
        if value == 1 and not visited[i][j]:
            board[i][j] = -1

for row in board:
    for val in row:
        print(val, end=" ")
    print()
