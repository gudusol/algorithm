import sys

input = sys.stdin.readline

N = [i for i in input().strip()]
M = int(input())
cursor = len(N)
stack = []

for _ in range(M):
    command = input().strip().split()
    if command[0] == "L":
        if len(N) > 0:
            stack.append(N.pop())
    elif command[0] == "D":
        if len(stack) > 0:
            N.append(stack.pop())
    elif command[0] == "B":
        if len(N) > 0:
            N.pop()
    elif command[0] == "P":
        char = command[1]
        N.append(char)

print("".join(N) + "".join(stack[::-1]))