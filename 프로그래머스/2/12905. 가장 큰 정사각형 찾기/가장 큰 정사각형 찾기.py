def solution(board):
    b = [[0] * (len(board[0]) + 2)]
    for i in board:  
        b.append([0] + i + [0])
    b.append([0] * (len(board[0]) + 2))
    
    m = 0
    for i in range(1, len(board) + 1):
        for j in range(1, len(board[0]) + 1):
            if b[i][j] != 0:
                b[i][j] = min(b[i - 1][j], b[i][j - 1], b[i - 1][j - 1]) + 1
                m = max(m, b[i][j])

    
    return m ** 2