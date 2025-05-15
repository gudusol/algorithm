import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, L, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False for _ in range(N)] for _ in range(N)]
unions = []
union = []
temp = 0
answer = 0

def dfs (row, col):
    global N, L, R, board, dx, dy, visited, union, temp
    for i in range(4):
        next_r, next_c = row + dx[i], col + dy[i]
        if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
            if L <= abs(board[row][col] - board[next_r][next_c]) <= R:
                union.append((next_r, next_c))
                visited[next_r][next_c] = True
                temp += board[next_r][next_c]
                dfs(next_r, next_c)


while True:
    unions = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for r, row in enumerate(board):
        for c, cur_count in enumerate(row):
            if not visited[r][c]:
                union = [(r, c)]
                visited[r][c] = True
                temp = board[r][c]
                dfs(r, c)
                if temp > cur_count:
                    unions.append([temp, union])
    if len(unions) == 0:
        break
    for count, rc in unions:
        div_count = count // len(rc)
        for r, c in rc:
            board[r][c] = div_count
    answer += 1
print(answer)