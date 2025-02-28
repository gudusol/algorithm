def solution(n, tops):
    dp1 = [0 for _ in range(n + 1)]
    dp2 = [0 for _ in range(n + 1)]
    
    if tops[0] == 1:
        dp1[1] = 3
        dp2[1] = 1
    else:
        dp1[1] = 2
        dp2[1] = 1

    for idx in range(2, n + 1):
        if tops[idx - 1] == 1:
            dp1[idx] = (dp1[idx - 1] * 3 + dp2[idx - 1] * 2) % 10007
        else:
            dp1[idx] = (dp1[idx - 1] * 2 + dp2[idx - 1]) % 10007
        dp2[idx] = (dp1[idx - 1] + dp2[idx - 1]) % 10007

    return (dp1[n] + dp2[n]) % 10007