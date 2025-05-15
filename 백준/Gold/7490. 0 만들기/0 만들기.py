import sys

input = sys.stdin.readline

T = int(input())


def dfs(idx, string):
    global results, arr
    if idx == len(arr):
        results.append(string)
        return

    dfs(idx + 1, string + "+" + str(arr[idx]))
    dfs(idx + 1, string + "-" + str(arr[idx]))
    dfs(idx + 1, string + " " + str(arr[idx]))


for _ in range(T):
    N = int(input())
    results = []
    answer = []
    arr = [i + 1 for i in range(N)]

    dfs(1, "1")
    for result in results:
        temp = ""
        prev = "+"
        ans = 0
        for s in result:
            if s == "+" or s == "-":
                ans = ans + int(temp) if prev == "+" else ans - int(temp)
                prev = s
                temp = ""
            elif s == ' ':
                continue
            else:
                temp += s
        ans = ans + int(temp) if prev == "+" else ans - int(temp)
        if ans == 0:
            answer.append(result)

    answer.sort()
    print(*answer, sep="\n")
    print()
