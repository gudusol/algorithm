def solution(n):
    num = format(n, 'b').count('1')
    n += 1
    while True:
        if format(n, 'b').count('1') == num:
            return n
        else:
            n += 1
