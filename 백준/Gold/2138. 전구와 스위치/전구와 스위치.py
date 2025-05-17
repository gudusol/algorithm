import sys
input = sys.stdin.readline

N = int(input())
start = [i for i in input().strip()]
end = [i for i in input().strip()]

answer = []

current = [*start]

def dp(count):
    global current
    for i in range(1, N - 1):
        if current[i - 1] != end[i - 1]:
            for j in range(i - 1, i + 2):
                current[j] =  '1' if current[j] == '0' else "0"
            count += 1
    if current[-2] == end[-2] and current[-1] == end[-1]:
        answer.append(count)
    elif current[-2] != end[-2] and current[-1] != end[-1]:
        answer.append(count + 1)
    return

dp(0)
current = [*start]
current[0] = '1' if current[0] == '0' else "0"
current[1] = '1' if current[1] == '0' else "0"
dp(1)

if len(answer) > 0:
    print(min(answer))
else:
    print(-1)