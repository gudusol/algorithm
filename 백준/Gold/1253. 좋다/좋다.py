import sys

input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

answer = 0
for idx, num in enumerate(numbers):
    left = 0
    right = N - 2

    numbers.pop(idx)
    while left < right:
        temp = numbers[left] + numbers[right]

        if num == temp:
            answer += 1
            break
        elif temp < num:
            left += 1
        elif temp > num:
            right -= 1

    numbers.append(num)
    numbers.sort()


print(answer)
