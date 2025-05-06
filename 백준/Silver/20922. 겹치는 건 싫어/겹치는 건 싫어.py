import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))

counter = defaultdict(int)
window = deque([])
answer = 0

current_length = 0

for n in numbers:
    if counter[n] == K:
        while True:
            pop_num = window.popleft()
            counter[pop_num] -= 1
            current_length -= 1
            if pop_num == n:
                break
    window.append(n)
    counter[n] += 1
    current_length += 1
    answer = max(answer, current_length)
print(answer)