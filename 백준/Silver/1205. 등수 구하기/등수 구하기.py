import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N, score, P = map(int, input().split())
scores = list(map(int, input().split())) if N > 0 else []
scores.reverse()

length = len(scores)

left_idx = bisect_left(scores, score)
right_idx = bisect_right(scores, score)

answer = length - right_idx + 1

if length == P:
    if left_idx == 0:
        answer = -1

print(answer)
