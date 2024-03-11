# def solution(word):
#     seq = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
#     answer = 0
#     for idx, w in enumerate(word.ljust(5, '0')):
#         if w != '0':
#             answer += 1
#             for _ in range(seq[w]):
#                 for power in range(5 - idx):
#                     answer += 5 ** power
                
#     return answer


from itertools import product

def solution(word):
    answer = 0
    all_word = list()
    words = ['A','E','I','O','U']
    for j in range(1,6):
        for i in product(words,repeat=j):
            all_word.append(list(i))
    all_word.sort()
    for i in all_word :
        answer += 1
        test_word = ''.join(s for s in i)
        if (test_word == word):
            break
    return answer