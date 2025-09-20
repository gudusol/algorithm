import sys

input = sys.stdin.readline

N, M = map(int, input().split())

init_board = []
board = []
cctvs = []
answer = N * M

for _ in range(N):
    line = list(map(int, input().split()))
    init_board.append(line)
    board.append(line)

for i, row in enumerate(init_board):
    for j, num in enumerate(row):
        if 1 <= num <= 5:
            cctvs.append([num, i, j])


def get_positions(num, row, col, dir):
    positions = [[], [], [], []]

    for i in range(row, -1, -1):
        if board[i][col] == 6:
            break
        elif board[i][col] == 0:
            positions[0].append([i, col])

    for i in range(col, M):
        if board[row][i] == 6:
            break
        elif board[row][i] == 0:
            positions[1].append([row, i])

    for i in range(row, N):
        if board[i][col] == 6:
            break
        elif board[i][col] == 0:
            positions[2].append([i, col])

    for i in range(col, -1, -1):
        if board[row][i] == 6:
            break
        elif board[row][i] == 0:
            positions[3].append([row, i])

    if num == 1:
        return [*positions[dir]]
    elif num == 2:
        opposite = (dir + 2) % 4
        return [*positions[dir], *positions[opposite]]
    elif num == 3:
        next = (dir + 1) % 4
        return [*positions[dir], *positions[next]]
    elif num == 4:
        next = (dir + 1) % 4
        nnext = (dir + 2) % 4
        return [*positions[dir], *positions[next], *positions[nnext]]
    elif num == 5:
        return sum(positions, [])


def add_cctv(pos_list):
    for r, c in pos_list:
        board[r][c] = "#"
    return


def remove_cctv(pos_list):
    for r, c in pos_list:
        board[r][c] = 0
    return


def dfs(idx):
    global answer
    if idx == len(cctvs):
        temp = 0
        for i in board:
            temp += i.count(0)
        answer = min(answer, temp)
        return

    num, x, y = cctvs[idx]
    for i in range(4):
        positions = get_positions(num, x, y, i)
        add_cctv(positions)
        dfs(idx + 1)
        remove_cctv(positions)


dfs(0)
print(answer)
