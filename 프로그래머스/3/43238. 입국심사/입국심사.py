def solution(n, times):
    start, end = 1, n * max(times)
    
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for t in times:
            people += mid // t
            
        if people >= n:
            end = mid - 1
        else:
            start = mid + 1
    return start