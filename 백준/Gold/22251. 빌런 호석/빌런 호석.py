import sys

input = sys.stdin.readline
N, K, P, X = map(int, input().split())
X = str(X)
X = '0' * (K - len(X)) + X

digit = {
    0: '1110111',
    1: '0010010',
    2: '1011101',
    3: '1011011',
    4: '0111010',
    5: '1101011',
    6: '1101111',
    7: '1010010',
    8: '1111111',
    9: '1111011',
}
diff = [[0 for _ in range(10)] for _ in range(10)]
for key, value in digit.items():
    digit[key] = int(value, 2)

for i in range(10):
    for j in range(i, 10):
        dif = bin(digit[i] ^ digit[j]).count('1')
        diff[i][j] = dif
        diff[j][i] = dif

answer = 0
def dfs(idx, result, string):
    global N, K, P, X, diff, answer
    if result > P:
        return
    if idx == K:
        if 0 < int(string) <= N:
            answer += 1
        return

    cur = X[idx]
    for ii, num in enumerate(diff[int(cur)]):
        new_string = string[:idx] + str(ii) + string[idx + 1:]
        dfs(idx + 1, result + num, new_string)



dfs(0, 0, X)
print(answer - 1)