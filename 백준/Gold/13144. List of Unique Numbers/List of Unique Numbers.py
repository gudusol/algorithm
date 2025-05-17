import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
visited = defaultdict(int)

answer = 0
left = 0

for right in range(N):
    while visited[numbers[right]] > 0:
        visited[numbers[left]] -= 1
        left += 1
    visited[numbers[right]] += 1
    answer += (right - left + 1)

print(answer)
