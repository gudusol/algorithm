import sys

input = sys.stdin.readline

string = input().strip()
bomb_input = input().strip()
bomb = [i for i in bomb_input]
bomb_len = len(bomb)

stack = []

for s in string:
    stack += s
    if stack[len(stack) - bomb_len : len(stack)] == bomb:
        for _ in range(bomb_len):
            stack.pop()

print(*stack, sep="") if len(stack) > 0 else print("FRULA")
