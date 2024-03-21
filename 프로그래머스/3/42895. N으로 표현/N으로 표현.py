def solution(N, number):
    dp = {}
    s = set()
    s.add(N)
    dp[N] = 1
    num = [s]     
    for index in range(7):
        temp = set()
        temp.add(int(str(N) * (index + 2)))
        dp[int(str(N) * (index + 2))] = index + 2
        for idx in range(len(num)):
            for i in num[idx]:
                for j in num[len(num) - 1 - idx]:
                    temp.add(i + j)
                    dp[i + j] = min(dp[i + j], dp[i] + dp[j]) if i + j in dp else dp[i] + dp[j]

                    temp.add(i - j)
                    dp[i - j] = min(dp[i - j], dp[i] + dp[j]) if i - j in dp else dp[i] + dp[j]

                    temp.add(i * j)
                    dp[i * j] = min(dp[i * j], dp[i] + dp[j]) if i * j in dp else dp[i] + dp[j]

                    if j != 0:
                        temp.add(i // j)
                        dp[i // j] = min(dp[i // j], dp[i] + dp[j]) if i // j in dp else dp[i] + dp[j]

#                     if i >= 0:
#                         double = int(str(i) + str(j))
                        
#                     if j >= 0:
#                         temp.add(double)
#                         dp[double] = min(dp[double], dp[i] + dp[j]) if double in dp else dp[i] + dp[j]

        num.append(temp)
        
    return dp[number] if number in dp else -1

# 1개 짜리 2중 포문으로 2개짜리 만들고
# 2개 짜리 2중 포문으로 4개짜리 만들고 => 1개 + 3개 
# 4개 짜리 2중 포문으로 8개짜리 만들고 => 3개 + 5개, 2개 + 6개, 1개 + 7
#                              => 얘네들이 고려가 안됐음
# 2 는 1개 연산 1개
# 3 은 1개 연산 2개, 2개 연산 1개
# 4 는 1개 연산 3개, 2개 연산 2개, 3개 연산 1개
# 5 는 1개 연산 4개, 2개 연산 3개, 3개 연산 2개, 4개 연산 1개
# ... 이런식으로 다 고려해줘야 할듯
