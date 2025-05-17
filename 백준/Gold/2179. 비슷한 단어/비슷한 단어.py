import sys

input = sys.stdin.readline

N = int(input())
words = [(input().strip(), i) for i in range(N)]
sorted_words = sorted(words)
max_length = 0
length = [0 for _ in range(N)]

for i in range(N - 1):
    cur, cur_idx = sorted_words[i]
    next, next_idx = sorted_words[i + 1]

    idx = 0
    len_cur = len(cur)
    len_next = len(next)

    while idx < len_cur and idx < len_next and cur[idx] == next[idx]:
        idx += 1
    if idx >= max_length:
        max_length = idx
        length[cur_idx] = idx
        length[next_idx] = idx

count = 0
pre = ""
index = 0
while length[index] != max_length:
    index += 1
print(words[index][0])
pre = words[index][0][:max_length]

index += 1
while True:
    if length[index] == max_length and words[index][0][:max_length] == pre:
        break
    index += 1
print(words[index][0])
