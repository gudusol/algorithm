def solution(n, times):
    low, hi = 1, n * max(times)
    print(low, hi)

    while low + 1 < hi:
        mid = (low + hi) // 2
        people = 0
        for t in times:
            people += mid // t
        print(1, low, mid, hi)

        if people >= n:
            hi = mid
        else:
            low = mid
        print(2, low, mid, hi)

    return hi