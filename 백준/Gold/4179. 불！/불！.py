import sys
import math
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [[-1 for _ in range(C + 2)] for _ in range(R + 2)]
visited = [[False for _ in range(C + 2)] for _ in range(R + 2)]

MAX_INT = math.inf

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

que = deque([])
x, y = 0, 9

for row in range(1, R + 1):
    line = input().strip()
    for col in range(1, len(line) + 1):
        s = line[col - 1]

        if s == "J":
            x, y = row, col
            board[row][col] = MAX_INT
        elif s == ".":
            board[row][col] = MAX_INT
        elif s == "F":
            que.append([row, col])
            board[row][col] = 0
        else:
            board[row][col] = -1

while que:
    cur_x, cur_y = que.popleft()

    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]

        if board[next_x][next_y] == MAX_INT:
            board[next_x][next_y] = board[cur_x][cur_y] + 1
            que.append([next_x, next_y])

que.append([x, y, 0])
visited[x][y] = True

while que:
    cur_x, cur_y, time = que.popleft()

    if cur_x == 1 or cur_y == 1 or cur_x == R or cur_y == C:
        print(time + 1)
        exit()

    for i in range(4):
        next_x, next_y = cur_x + dx[i], cur_y + dy[i]

        if not visited[next_x][next_y] and board[next_x][next_y] > time + 1:
            visited[next_x][next_y] = True
            que.append([next_x, next_y, time + 1])

print("IMPOSSIBLE")
