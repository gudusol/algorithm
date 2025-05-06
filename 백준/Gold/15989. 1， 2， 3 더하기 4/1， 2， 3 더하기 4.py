import sys

input = sys.stdin.readline

T = int(input())
numbers = [int(input()) for _ in range(T)]

dp = [1] * (max(numbers) + 1)

for i in range(2, len(dp)):
    dp[i] += dp[i - 2]

for i in range(3, len(dp)):
    dp[i] += dp[i - 3]

for n in numbers:
    print(dp[n])
