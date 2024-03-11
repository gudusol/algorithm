from math import floor
from itertools import permutations
                
def solution(numbers):
    permute_list = sum([list(permutations(numbers, i)) for i in range(1, len(numbers) + 1)], [])
    numbers_list = set(map(lambda x: int(''.join(list(x))), permute_list))
    if 0 in numbers_list: numbers_list.remove(0)
    if 1 in numbers_list: numbers_list.remove(1)
    for i in range(2, floor(max(numbers_list) ** 0.5)):
        for j in range(i * 2, max(numbers_list) + 1, i):
            if j in numbers_list:
                numbers_list.remove(j)
    
    return len(numbers_list)