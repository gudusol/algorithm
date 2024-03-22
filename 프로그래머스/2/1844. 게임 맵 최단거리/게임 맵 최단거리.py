from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    new_maps = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            new_maps[i][j] = -1 if maps[i - 1][j - 1] == 1 else 0
            
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
        
    que = deque([[1, 1]])
    new_maps[1][1] = 1
    while que:
        x, y = que.popleft()
        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            if new_maps[cur_x][cur_y] == -1:
                que.append([cur_x, cur_y])
                new_maps[cur_x][cur_y] = new_maps[x][y] + 1
            else:
                new_maps[cur_x][cur_y] = min(new_maps[cur_x][cur_y], new_maps[x][y] + 1)
    return new_maps[n][m]
