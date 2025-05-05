import sys

input = sys.stdin.readline

S = [i for i in input().strip()]
zero_count = S.count("0") // 2
one_count = S.count("1") // 2

for _ in range(one_count):
    S.remove("1")
S = S[::-1]
for _ in range(zero_count):
    S.remove("0")

print("".join(S[::-1]))
