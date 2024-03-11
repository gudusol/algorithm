def solution(word):
    seq = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = 0
    for idx, w in enumerate(word.ljust(5, '0')):
        if w != '0':
            answer += 1
            for _ in range(seq[w]):
                for power in range(5 - idx):
                    answer += 5 ** power
    return answer