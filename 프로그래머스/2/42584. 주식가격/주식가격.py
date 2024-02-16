def solution(prices):
    answer = []
    for i, v in enumerate(prices):
        time = 0
        cur = v
        for j in range(i, len(prices) - 1):
            if v > prices[j]:
                break
            else:
                time += 1
        answer.append(time)
    return answer