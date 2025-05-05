import sys

input = sys.stdin.readline

N, D = map(int, input().split())
short = [list(map(int, input().split())) for _ in range(N)]
short.sort()

answer = []


def dfs(current, total):
    global short

    if current > D:
        return
    answer.append(total + (D - current))
    for start, end, distance in short:
        if current <= start:
            dfs(end, total + (start - current) + distance)

dfs(0, 0)
print(min(answer))
