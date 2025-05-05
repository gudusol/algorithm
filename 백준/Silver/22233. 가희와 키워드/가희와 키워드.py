import sys

input = sys.stdin.readline

N, M = map(int, input().split())

notepad = set(input().strip() for _ in range(N))

for _ in range(M):
    keywords = set(input().strip().split(","))
    notepad -= keywords

    print(len(notepad))
