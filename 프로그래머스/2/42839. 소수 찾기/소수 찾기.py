from math import floor
from itertools import permutations

def eratos(num):
    li = [True for i in range(num + 1)]
    li[0] = False
    li[1] = False
    for i in range(2, floor(num ** 0.5)):
        for j in range(i * 2, num + 1, i):
            if li[j]:
                li[j] = False
    return li
                
def solution(numbers):
    max_num = int(''.join(sorted([i for i in numbers], reverse=True)))
    eratos_list = eratos(max_num)
    permute_list = sum([list(permutations(numbers, i)) for i in range(1, len(numbers) + 1)], [])
    numbers_list = set(map(lambda x: int(''.join(list(x))), permute_list))
    
    count = 0
    for n in numbers_list:
        if eratos_list[n]:
            count += 1
    return count