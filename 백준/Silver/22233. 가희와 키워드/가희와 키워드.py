import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())
notepad = defaultdict(bool)
for _ in range(N):
    notepad[input().strip()] = True

answer = len(notepad)

for _ in range(M):
    keywords = input().strip().split(",")
    for k in keywords:
        if notepad[k]:
            notepad[k] = False
            answer -= 1

    print(answer)
