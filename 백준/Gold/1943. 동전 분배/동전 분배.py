import sys

input = sys.stdin.readline


for _ in range(3):
    N = int(input())

    coins = []
    total = 0
    for _ in range(N):
        coin = list(map(int, input().split()))
        coins.append(coin)
        total += coin[0] * coin[1]
    if total % 2 != 0:
        print(0)
        continue
    target = total // 2

    dp = [False for _ in range(target + 1)]
    dp[0] = True

    for price, count in coins:
        for i in range(len(dp) - 1, price - 1, -1):
            if dp[i - price]:
                for j in range(count):
                    if i + price * j <= target:
                        dp[i + price * j] = True
                    else:
                        break
                if dp[target]:
                    break

    print(1) if dp[target] else print(0)
