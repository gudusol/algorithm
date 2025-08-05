import sys

input = sys.stdin.readline

N = int(input())
height = list(map(int, input().split()))

answer = [{"count": 0, "left_idx": -1, "right_idx": -1} for _ in range(N)]

stack = []

for idx, h in enumerate(height):
    while len(stack) > 0 and stack[-1][1] <= h:
        stack.pop()
    if len(stack) > 0:
        answer[idx]["count"] += len(stack)
        answer[idx]["left_idx"] = stack[-1][0]
    stack.append([idx, h])

stack = []
reverse_height = height[::-1]
for idx, h in enumerate(reverse_height):
    while len(stack) > 0 and stack[-1][1] <= h:
        stack.pop()
    if len(stack) > 0:
        answer[N - idx - 1]["count"] += len(stack)
        answer[N - idx - 1]["right_idx"] = stack[-1][0]
    stack.append([N - idx - 1, h])


for cur_idx, dict in enumerate(answer):
    count, left_idx, right_idx = dict["count"], dict["left_idx"], dict["right_idx"]
    print(count, end=" ")

    closest_idx = []

    if left_idx != -1:
        closest_idx.append([abs(left_idx - cur_idx), left_idx])
    if right_idx != -1:
        closest_idx.append([abs(right_idx - cur_idx), right_idx])

    closest_idx.sort()
    if len(closest_idx) > 0:
        print(closest_idx[0][1] + 1)
    else:
        print()
