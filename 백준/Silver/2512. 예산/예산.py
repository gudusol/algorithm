import sys

input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
total = int(input())

left = 0
right = max(req)
temp = 0
answer = 0

while left <= right:
    mid = (left + right) // 2

    temp = 0
    for budget in req:
        if budget >= mid:
            temp += mid
        else:
            temp += budget

    if temp > total:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
