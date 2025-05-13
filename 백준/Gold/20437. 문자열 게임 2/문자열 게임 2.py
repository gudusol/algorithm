import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    W = input().strip()
    K = int(input())
    counter = defaultdict(int)
    index_dict = defaultdict(list)
    for key, value in Counter(W).items():
        if value >= K:
            counter[key] = value
    if len(counter) == 0:
        print(-1)
        continue

    for idx, w, in enumerate(W):
        if counter[w] > 0:
            index_dict[w].append(idx)

    temp = []
    for li in index_dict.values():
        for i in range(len(li) - K + 1):
            temp.append(li[i + K - 1] - li[i] + 1)

    print(min(temp), max(temp))
