import sys

input = sys.stdin.readline

N, C = map(int, input().split(" "))
houses = []

for i in range(N):
    houses.append(int(input()))
houses.sort()

lo = 1
hi = houses[-1] - houses[0]
result = 0

while lo <= hi:
    mid = (lo + hi) // 2

    prev_house = houses[0]
    count = 1
    for i in range(1, len(houses)):
        if houses[i] - prev_house >= mid:
            count += 1
            prev_house = houses[i]

    if count < C:
        hi = mid - 1
    else:
        lo = mid + 1

print(hi)
