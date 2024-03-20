def solution(number, k):
    n = [int(i) for i in number][::-1]
    stack = []
    for _ in range(k):
        for _ in range(len(n)):
            if not stack:
                stack.append(n.pop())
            else:
                if stack[-1] < n[-1]:
                    stack.pop()
                    break
                else:
                    stack.append(n.pop())
    while stack:
        n.append(stack.pop())
    n = n[::-1]
    while len(n) > len(number) - k:
        n.pop()
    return "".join(map(str, n))