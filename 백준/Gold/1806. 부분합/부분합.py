import sys

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

left, right = 0, 0
length = 1
answer = []
acc = numbers[0]

while right < N - 1:
    while acc < S and right < N - 1:
        right += 1
        length += 1
        acc += numbers[right]
    while acc >= S and left <= right:
        answer.append(length)

        acc -= numbers[left]
        length -= 1
        left += 1

print(min(answer)) if len(answer) else print(0)
