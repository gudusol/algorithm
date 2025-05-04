import sys

input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

cur_idx = 0
next_idx = 0
temp = 0

answer = 0

while True:
    if next_idx == N - 1:
        answer += temp * cost[cur_idx]
        break

    if cost[next_idx] < cost[cur_idx]:
        answer += temp * cost[cur_idx]
        temp = 0
        cur_idx = next_idx

    next_idx += 1
    temp += distance[next_idx - 1]

print(answer)
