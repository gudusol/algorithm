import math
from itertools import product
from bisect import bisect_left

def solution(users, emoticons):
    answer = [0, 0]
    percent = [10, 20, 30, 40]
    percent_arr = [percent for _ in range(len(emoticons))]
    discounts = list(product(*percent_arr))
    
    for discount in discounts:
        plus = 0
        profit = 0
        for user_percent, user_price in users:
            total = 0
            for idx, emoticon_price in enumerate(emoticons):
                if user_percent <= discount[idx]:
                    total += (emoticon_price * (100 - discount[idx])) // 100
            if user_price <= total:
                plus += 1
            else:
                profit += total
                
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = profit
        elif answer[0] == plus:
            if answer[1] < profit:
                answer[1] = profit   
    return answer