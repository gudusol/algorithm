def solution(money):
    ans = []
    
    for momey_arr in [money[1:], money[:-1]]:
        dp = [0 for _ in range(len(momey_arr))]
    
        dp[0] = momey_arr[0]
        dp[1] = max(momey_arr[0], momey_arr[1])
        dp[2] = max(momey_arr[0] + momey_arr[2], momey_arr[1])

        for i in range(3, len(momey_arr)):
            dp[i] = max(dp[i - 3] + momey_arr[i] , dp[i - 2] + momey_arr[i], dp[i - 1])
        ans.append(dp[-1])

    return max(ans)