str_1 = input()
str_2 = input()

dp = [['' for _ in range(len(str_2) + 1)] for _ in range(len(str_1) + 1)]

for idx_1 in range(1, len(str_1) + 1):
    for idx_2 in range(1, len(str_2) + 1):
        if idx_1 == 0 or idx_2 == 0:
            continue
        elif str_1[idx_1 - 1] == str_2[idx_2 - 1]:
            dp[idx_1][idx_2] = dp[idx_1 - 1][idx_2 - 1] + str_1[idx_1 - 1]
        else:
            dp[idx_1][idx_2] = dp[idx_1 - 1][idx_2] if len(dp[idx_1 - 1][idx_2]) >= len(dp[idx_1][idx_2 - 1]) else dp[idx_1][idx_2 - 1]

lcs = dp[-1][-1]
print(len(lcs))
if len(lcs) != 0:
    print(lcs)
