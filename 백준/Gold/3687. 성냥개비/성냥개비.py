import sys
import math

input = sys.stdin.readline

T = int(input())
numbers = [int(input()) for _ in range(T)]
dp = [math.inf for _ in range(max(max(numbers) + 1, 8))]

num_count = {2: "1", 3: "7", 4: "4", 5: "2", 6: "0", 7: "8"}

for c in num_count:
    dp[c] = int(num_count[c])
dp[6] = 6
dp[8] = 10

for i in range(9, len(dp)):
    for k, v in num_count.items():
        if k == 6:
            dp[i] = min(dp[i], int(str(dp[i - k]) + v))
        else:
            dp[i] = min(dp[i], int(str(dp[i - k]) + v), int(v + str(dp[i - k])))

for num in numbers:
    answer_max = ""

    if num % 2 == 0:
        answer_max = "1" * (num // 2)
    else:
        answer_max = "7" + "1" * (num // 2 - 1)

    print(dp[num], answer_max)
