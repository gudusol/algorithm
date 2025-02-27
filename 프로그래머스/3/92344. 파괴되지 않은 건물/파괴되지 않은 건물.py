def solution(board, skill):
    answer = 0
    new_board = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    for skill_type, r1, c1, r2, c2, degree in skill:
        value = degree if skill_type == 2 else degree * -1
        
        new_board[r1][c1] += value
        new_board[r1][c2 + 1] -= value
        new_board[r2 + 1][c1] -= value
        new_board[r2 + 1][c2 + 1] += value
    
    for r in range(len(new_board)):
        for c in range(1, len(new_board[0])):
            new_board[r][c] += new_board[r][c - 1]

    for r in range(1, len(new_board)):
        for c in range(len(new_board[0])):
            new_board[r][c] += new_board[r - 1][c]
            
    for r, row in enumerate(board):
        for c, value in enumerate(row):
            if board[r][c] + new_board[r][c] > 0:
                answer += 1
    return answer