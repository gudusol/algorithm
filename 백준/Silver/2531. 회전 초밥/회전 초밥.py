import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]

answer = []
for i in range(k - 1):
    sushi.append(sushi[i])

for i in range(N):
    answer.append(len(set(sushi[i : i + k] + [c])))

print(max(answer))
