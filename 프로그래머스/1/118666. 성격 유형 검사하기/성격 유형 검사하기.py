def solution(survey, choices):
    alpha = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    result = {i: 0 for i in sum(alpha, [])}
    
    for i, s in enumerate(survey):
        score = choices[i]
        if 1 <= score <= 3:
            result[s[0]] += (4 - score)
        elif 5 <= score <= 7:
            result[s[1]] += (score - 4)
    
    answer = ''
    for a, b in alpha:
        if result[a] < result[b]:
            answer += b
        else:
            answer += a

    return answer