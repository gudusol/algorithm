from itertools import permutations

def solution(k, dungeons):
    cases = list(permutations(dungeons, len(dungeons)))
    answers = []
    for case in cases:
        answer = 0
        current = k
        for req, consume in case:
            if current >= req:
                current -= consume
                answer += 1
        if answer == len(dungeons):
            return answer
        answers.append(answer)
                
    return max(answers)