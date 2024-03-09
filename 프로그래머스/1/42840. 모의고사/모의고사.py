def solution(answers):
    score = {1: 0, 2: 0, 3: 0}
    pattern_list = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    iter_list = [0, 0, 0]
    
    for num in answers:
        for idx, pattern in enumerate(pattern_list):
            if num == pattern[iter_list[idx]]:
                score[idx + 1] += 1
        iter_list = list(map(lambda x: x+1, iter_list))
        
        for idx, iterate in enumerate(iter_list):
            if iterate == len(pattern_list[idx]):
                iter_list[idx] = 0
    
    answer = []
    result = sorted(score.items(), key= lambda x: x[1], reverse=True)
    max_val = result[0][1]
    for num, score in result:
        if score == max_val:
            answer.append(num)

    return answer