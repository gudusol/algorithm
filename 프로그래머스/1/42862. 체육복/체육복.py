def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    li = [True] * n
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            continue
        li[i - 1] = False
    for i in reserve:
        for j in [-1, 0, 1]:
            index = i + j - 1
            if index < 0 or index >= n:
                continue
            if not li[index]:
                li[index] = True
                break
    return li.count(True)