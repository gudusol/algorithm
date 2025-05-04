import sys

input = sys.stdin.readline

N, K = map(int, input().split())
table = []
answer = 0
for i in input().strip():
    table.append(i)

for idx, val  in enumerate(table):
    if val == 'P':
        for i in range(idx - K, idx + K + 1):
            if 0 <= i < N and table[i] == "H":
                table[i] = "-"
                answer += 1
                break

print(answer)