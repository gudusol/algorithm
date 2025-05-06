import sys

input = sys.stdin.readline

string = input().strip()

a = string.count("a")
b = string.count("b")

answer = []

for i in range(len(string) - a):
    answer.append(a - string[i : i + a].count('a'))

for i in range(len(string) - b):
    answer.append(b - string[i : i + b].count('b'))

print(min(answer))
