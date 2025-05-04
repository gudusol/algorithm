import sys

input = sys.stdin.readline

words = {}
N, M = map(int, input().split())
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
sorted_words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in sorted_words:
    print(i[0])
