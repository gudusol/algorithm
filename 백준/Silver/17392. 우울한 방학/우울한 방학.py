import sys

input = sys.stdin.readline

N, M = map(int, input().split())
if N == 0:
    answer = 0
    for i in range(1, M + 1):
        answer += i ** 2
    print(answer)
else:
    happy = list(map(int, input().split()))

    happy_count = len(happy)
    unhappy_day = M - sum([i + 1 for i in happy])

    unhappy = [unhappy_day // (happy_count + 1) for _ in range(happy_count + 1)]
    for i in range(unhappy_day % (happy_count + 1)):
        unhappy[i] += 1

    answer = 0
    for u in unhappy:
        for i in range(u + 1):
            answer += i ** 2


    print(answer)