import sys

input = sys.stdin.readline

N = int(input())
plans = [list(map(int, input().split())) for _ in range(N)]

calandar = [0 for _ in range(1, 367)]

for start, end in plans:
    for d in range(start, end + 1):
        calandar[d] += 1

answer = 0
height = 0
width = 0

for c in calandar:
    if c == 0:
        answer += height * width
        height = 0
        width = 0
    else:
        width += 1
        height = max(height, c)
answer += height * width

print(answer)
