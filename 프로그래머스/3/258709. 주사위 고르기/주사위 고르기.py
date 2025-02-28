from itertools import combinations, product
from bisect import bisect_left
def solution(dice):
    n = len(dice)
    results = []
    for a_com in combinations(range(1, n + 1), n // 2):
        b_com = list(filter(lambda x: x not in a_com, range(1, n + 1)))
        
        a_cases = product(*[dice[i - 1] for i in a_com])
        b_cases = product(*[dice[i - 1] for i in b_com])
        a_sum = sorted([sum(i) for i in a_cases])
        b_sum = sorted([sum(i) for i in b_cases])
        
        results.append([a_com, 0])
        for a_num in a_sum:
            results[-1][1] += bisect_left(b_sum, a_num)
    
    results.sort(key = lambda x: x[1], reverse=True)
    return list(results[0][0])