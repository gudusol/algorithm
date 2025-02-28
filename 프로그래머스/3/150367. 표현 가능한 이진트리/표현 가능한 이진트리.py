import sys
sys.setrecursionlimit(10**6)

def check(string):
    if len(string) == 1:
        return True
    center_idx = len(string) // 2
    if string[center_idx] == '0':
        if '1' in string:
            return False
    else:
        if len(string) == 3:
            return True
    if not check(string[:center_idx]) or not check(string[center_idx+1:]):
        return False
    
    return True


def solution(numbers):
    answer = []
    for num in numbers:
        bi_str = str(bin(num)[2:])
        length = len(bi_str)
        n = 0
        while True:
            if 2**n - 1 < length <= 2**(n+1) - 1:
                bi_str = ('0' * (2**(n+1) - 1 - length)) + bi_str
                break
            n += 1
        
        if check(bi_str):
            answer.append(1)
        else:
            answer.append(0)

    return answer