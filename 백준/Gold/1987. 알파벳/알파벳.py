import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(R)]
answer = 0

stack = set()
stack.add((0, 0, board[0][0]))
while stack:
    r, c, path = stack.pop()
    is_end = True

    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]
        if 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in path:
            stack.add((nr, nc, path + board[nr][nc]))
            is_end = False
    if is_end:
        answer = max(answer, len(path))


print(answer)
