import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
words = defaultdict(list)
for _ in range(N):
    w = input().strip()
    words[w[0]].append(w)
answer = 0
S = ''
T = ''

for word_list in words.values():
    for i in range(len(word_list)):
        for j in range(i+1, len(word_list)):
            cur_s = word_list[i]
            cur_t = word_list[j]

            idx = 0
            len_cur_s = len(cur_s)
            len_cur_t = len(cur_t)
            while idx < len_cur_s and idx < len_cur_t and cur_s[idx] == cur_t[idx]:
                idx += 1
            
            if idx > answer:
                answer = idx
                S = cur_s
                T = cur_t

print(S)
print(T)