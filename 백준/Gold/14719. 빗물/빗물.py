import sys

input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))
answer = 0
for i in range(1, W - 1):
    left_top = max(height[:i])
    right_top = max(height[i+1:])
    cur = height[i]

    if cur <= left_top and cur <= right_top:
        gap  = min(left_top, right_top) - cur
        answer += gap
print(answer)