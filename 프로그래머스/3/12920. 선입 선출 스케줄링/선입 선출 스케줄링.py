def solution(n, cores):
    n -= len(cores)
    if n <= 0:
        return 0
    lo = 0
    hi = n * max(cores)
    
    while lo + 1 < hi:
        p = 0
        mid = (lo + hi) // 2
        for c in cores:
            p += mid // c
            
        if p >= n:
            hi = mid
        else:
            lo = mid
    for idx, c in enumerate(cores):
        n -= lo // c
        # remain = hi % c
        # cores[idx] = remain if remain == 0 else c - remain
    
    # for idx, c in enumerate(cores):
    #     if c == 0:
    #         n -= 1
    #         if n == 0:
    #             return idx + 1
    
    for idx, c in enumerate(cores):
        if hi % c == 0:
            n -= 1
            if n == 0:
                return idx + 1
    return
