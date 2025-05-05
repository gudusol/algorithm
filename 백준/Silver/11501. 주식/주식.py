import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    price = price[::-1]

    cur = price[0]
    answer = 0 
    temp = 0
    for p in price:
        if p > cur:
            answer += temp
            temp = 0
            cur = p
        else:
            temp += (cur - p)

    answer += temp
    print(answer)