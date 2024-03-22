def solution(m, n, puddles):
    arr = [[0] * (n + 2) for _ in range(m + 2)]
    arr[1][1] = 1
    for x, y in puddles:
        arr[x][y] = -1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if arr[i][j] == -1 or (i == 1 and j == 1):
                continue
                
            if arr[i - 1][j] != -1 and arr[i][j - 1] != -1:
                arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
            elif arr[i - 1][j] == -1:
                arr[i][j] = arr[i][j - 1]
            elif arr[i][j - 1] == -1:
                arr[i][j] = arr[i - 1][j]
            elif arr[i - 1][j] == -1 and arr[i][j - 1] == -1:
                arr[i][j] = 0

    return arr[m][n] % 1000000007