N, K = map(int, input().split())
items = []

for _ in range(N):
    w, v = map(int, input().split())
    items.append([w, v])

dp = [[0 for _ in range(K + 1)] for _ in range(N)]
for i in range(len(dp[0])):
    if items[0][0] <= i:
        dp[0][i] = items[0][1]

for i in range(1, len(dp)):
    for j, w in enumerate(dp[i]):
        if items[i][0] <= j:
            dp[i][j] = max(dp[i - 1][j], items[i][1] + dp[i - 1][j - items[i][0]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N - 1][K])
