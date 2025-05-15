import sys

input = sys.stdin.readline

N = int(input())
num = [int(input()) for _ in range(N)]

cycles = []
for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]

    visited[i] = True
    cur = i
    temp = [cur]
    while True:
        next = num[cur - 1]
        if next == i:
            cycles.append(*temp)
            break
        else:
            if not visited[next]:
                visited[next] = True
                cur = next
            else:
                break
print(len(cycles))
print(*cycles, sep="\n")
