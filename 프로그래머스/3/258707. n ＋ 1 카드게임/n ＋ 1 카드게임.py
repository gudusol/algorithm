from collections import deque
from itertools import combinations, product
    
def solution(coin, cards):
    n = len(cards)
    cur_cards = cards[:n // 3]
    cards = deque(cards[n // 3:])
    coin_cards = []
    turn = 0
    
    while True:
        is_break = False
        turn += 1
        if len(cards) == 0:
            return turn
        coin_cards.append(cards.popleft())
        coin_cards.append(cards.popleft())
        
        for a, b in combinations(cur_cards, 2):
            if a + b == n + 1:
                cur_cards.remove(a)
                cur_cards.remove(b)
                is_break = True
                break
        if is_break:
            continue
            
        for a, b in product(cur_cards, coin_cards):
            if a + b == n + 1:
                cur_cards.remove(a)
                coin_cards.remove(b)
                if coin < 1:
                    return turn
                coin -= 1
                is_break = True
                break
        if is_break:
            continue
            
        for a, b in combinations(coin_cards, 2):
            if a + b == n + 1:
                coin_cards.remove(a)
                coin_cards.remove(b)
                if coin < 2:
                    return turn
                coin -= 2
                is_break = True
                break
        if is_break:
            continue
            
        return turn