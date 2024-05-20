dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global M, N, dx, dy, board, visited, dp

    if visited[x][y]:
        return dp[x][y]
    if x == M and y == N:
        return 1

    visited[x][y] = True
    case = 0
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if board[next_x][next_y] != 0 and board[next_x][next_y] < board[x][y]:
            case += dfs(next_x, next_y)
    dp[x][y] = case
    return case


M, N = map(int, input().split())
input_board = []
for i in range(M):
    input_board.append(list(map(int, input().split())))

board = [[0 for _ in range(N + 2)] for _ in range(M + 2)]
visited = [[False for _ in range(N + 2)] for _ in range(M + 2)]
dp = [[0 for _ in range(N + 2)] for _ in range(M + 2)]
for i in range(M):
    for j in range(N):
        board[i + 1][j + 1] = input_board[i][j]

print(dfs(1, 1))
