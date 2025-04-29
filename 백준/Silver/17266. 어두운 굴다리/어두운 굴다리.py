import sys
import math

input = sys.stdin.readline

N = int(input())
M = int(input())
locations = list(map(int, input().split()))
distance = []

left = locations[0]
right = N - locations[M - 1]

prev = locations[0]

for x_idx in range(1, M):
    x = locations[x_idx]
    distance.append(x - prev)
    prev = x

temp = 0
if len(distance) > 0:
    temp = math.ceil(max(distance) / 2)

print(max(left, right, temp))
