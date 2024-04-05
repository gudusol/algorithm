def solution(land):
    dp = [[0,0,0,0] for _ in range(len(land))]
    for idx, arr in enumerate(land):
        for i, num in enumerate(arr):
            if idx == 0:
                dp[idx][i] = land[idx][i]
            else:
                dp[idx][i] = num + max(dp[idx - 1][:i] + dp[idx - 1][i + 1:])
    return max(dp[-1])