import sys

input = sys.stdin.readline

A, B = map(int, input().split())


def count(num):
    binary = bin(num)[2:]
    ans = 0
    length = len(binary)
    count_one = 0

    for idx in range(length - 1):
        if binary[idx] == "1":
            x = length - idx - 1
            ans += 2 ** (x - 1) * x + 1
            ans += count_one * 2**x
            count_one += 1
    ans += int(binary[-1]) * (count_one + 1)
    return ans


print(count(B) - count(A - 1))
