import sys

input = sys.stdin.readline

N = int(input())
word = input().strip()
words = [input().strip() for _ in range(N - 1)]
answer = 0

for w in words:
    not_found = []
    cur_word = [i for i in w]
    for i in word:
        if i in cur_word:
            cur_word.remove(i)
        else:
            not_found.append(i)
    len_cur = len(cur_word)
    len_not_found = len(not_found)
    if (len_cur == 1 and len_not_found == 1) or (len_cur + len_not_found <= 1):
        answer += 1

print(answer)
