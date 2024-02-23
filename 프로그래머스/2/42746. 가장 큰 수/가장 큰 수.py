def solution(numbers):
    n = [str(num)*4 for num in numbers]
    sorted_arr = sorted(n, key=lambda x: x, reverse=True)
    s = ''
    for value in sorted_arr:
        s += value[:len(value) // 4]
    
    return str(int(s))