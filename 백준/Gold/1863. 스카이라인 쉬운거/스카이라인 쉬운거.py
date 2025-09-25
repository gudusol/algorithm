import sys

input = sys.stdin.readline


N = int(input())
stack = []
answer = 0

for _ in range(N):
    x, y = map(int, input().split())

    if len(stack) == 0:
        if y > 0:
            stack.append(y)
    else:
        top = stack[-1]

        if top < y:
            stack.append(y)
        else:
            while True:
                if len(stack) > 0 and top > y:
                    stack.pop()
                    answer += 1
                    if len(stack) == 0:
                        if y > 0:
                            stack.append(y)
                            top = stack[-1]
                        break
                    else:
                        top = stack[-1]
                elif top == y:
                    break
                else:
                    stack.append(y)
                    top = stack[-1]
                    break

answer += len(stack)

print(answer)
