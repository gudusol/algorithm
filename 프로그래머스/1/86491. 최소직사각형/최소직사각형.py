def solution(sizes):
    size_long = []
    size_short = []
    for w, h in sizes:
        size_long.append(max(w,h))
        size_short.append(min(w,h))
    
    return max(size_long) * max(size_short)