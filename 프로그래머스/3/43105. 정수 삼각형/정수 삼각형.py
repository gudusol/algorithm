def solution(triangle):
    dp = [[0] * i for i in range(1, len(triangle) + 1)]
    dp[0][0] = triangle[0][0]
    for line, numbers in enumerate(triangle):
        if line == len(triangle) - 1:
            break
        for idx, num in enumerate(numbers):
            dp[line + 1][idx] = max(dp[line + 1][idx], dp[line][idx] + triangle[line + 1][idx])
            dp[line + 1][idx + 1] = max(dp[line + 1][idx + 1], dp[line][idx] + triangle[line + 1][idx + 1])
            
    return max(dp[-1])