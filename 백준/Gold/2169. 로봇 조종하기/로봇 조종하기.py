import sys

input = sys.stdin.readline

MIN_NUM = -100000000

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = board[0][0]

for i in range(1, M):
    dp[0][i] = dp[0][i - 1] + board[0][i]

for i in range(1, N):
    leftToRight = [MIN_NUM for _ in range(M)]
    rightToLeft = [MIN_NUM for _ in range(M)]

    leftToRight[0] = dp[i - 1][0] + board[i][0]
    rightToLeft[M - 1] = dp[i - 1][M - 1] + board[i][M - 1]
    for j in range(1, M):
        leftToRight[j] = max(leftToRight[j - 1], dp[i - 1][j]) + board[i][j]
    for j in range(M - 2, -1, -1):
        rightToLeft[j] = max(rightToLeft[j + 1], dp[i - 1][j]) + board[i][j]

    for j in range(M):
        dp[i][j] = max(leftToRight[j], rightToLeft[j])

print(dp[N - 1][M - 1])
