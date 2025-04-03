import sys

input = sys.stdin.readline

def get_length(cur_x, cur_y, dx, dy):
    global board

    length = 0
    while board[cur_x][cur_y] == 1:
        length += 1
        cur_x += dx
        cur_y += dy

    return cur_x, cur_y, length


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [[0 for _ in range(N + 2)] for _ in range(N + 2)]

for i in range(1, N + 1):
    line = input().strip()

    for j in range(len(line)):
        board[i][j + 1] = 0 if line[j] == "_" else 1

heart_x, heart_y = 0, 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if board[i][j] == 1:
            is_heart = True
            for di in range(4):
                if board[i + dx[di]][j + dy[di]] != 1:
                    is_heart = False
                    break
            if is_heart:
                heart_x, heart_y = i, j
                break

answer = []
leg_x, leg_y = 0, 0

x, y, length = get_length(heart_x, heart_y - 1, dx[3], dy[3])
answer.append(length)
x, y, length = get_length(heart_x, heart_y + 1, dx[1], dy[1])
answer.append(length)
x, y, length = get_length(heart_x + 1, heart_y, dx[2], dy[2])
leg_x, leg_y = x - 1, y
answer.append(length)
x, y, length = get_length(leg_x + 1, leg_y - 1, dx[2], dy[2])
answer.append(length)
x, y, length = get_length(leg_x + 1, leg_y + 1, dx[2], dy[2])
answer.append(length)

print(heart_x, heart_y)
print(*answer, sep=" ")
