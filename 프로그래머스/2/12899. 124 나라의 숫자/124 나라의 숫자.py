def solution(n):
    num = n
    remain = []
    while num > 0:
        r = num % 3
        if r == 0:
            r = 4
            num -= 1
        remain.append(str(r))
        num = num // 3

    return ''.join(remain[::-1])