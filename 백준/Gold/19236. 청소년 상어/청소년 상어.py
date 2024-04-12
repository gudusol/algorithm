def move_fish(cur_board):
    global dx, dy
    for i in range(1, 17):
        is_move = False

        for x in range(4):
            for y in range(4):
                if cur_board[x][y][0] != i:
                    continue
                else:
                    num, di = cur_board[x][y][0], cur_board[x][y][1]
                    for _ in range(8):
                        if di > 8:
                            di -= 8
                        next_x, next_y = x + dx[di], y + dy[di]  # 다음 좌표

                        if 0 <= next_x <= 3 and 0 <= next_y <= 3:  # 판 안에 있고
                            next_num = cur_board[next_x][next_y][0]
                            if next_num == -1:  # 상어 있음
                                pass
                            elif next_num == 0:  # 빈 칸
                                cur_board[next_x][next_y][0], cur_board[next_x][next_y][1] = num, di
                                cur_board[x][y][0], cur_board[x][y][1] = 0, 0
                                is_move = True
                                break

                            else:  # 물고기 있음
                                cur_board[x][y][0], cur_board[x][y][1] = cur_board[next_x][next_y][0], cur_board[next_x][next_y][1]
                                cur_board[next_x][next_y][0], cur_board[next_x][next_y][1] = num, di
                                is_move = True
                                break
                        di += 1
                    if is_move:
                        break
            if is_move:
                break


def init_shark():
    global board
    fish_num = board[0][0][0]
    board[0][0][0] = -1
    return fish_num

def shark_xy(board):
    for x in range(4):
        for y in range(4):
            if board[x][y][0] == -1:
                return x, y


def move_shark(board, ans):
    global dx, dy, ans_list

    shark_x, shark_y = shark_xy(board)

    cur_ans = ans
    cur_board = []
     # 판 복사
    for row in board:
        temp = []
        for xy in row:
            temp.append(xy[:])
        cur_board.append(temp)


    move_fish(cur_board)

    di = cur_board[shark_x][shark_y][1]
    next_x = shark_x
    next_y = shark_y
    cur_board[shark_x][shark_y] = [0, 0]

    is_eat = False
    while 0 <= next_x <= 3 and 0 <= next_y <= 3:
        if cur_board[next_x][next_y][0] > 0:  # 물고기 있음
            is_eat = True
            fish_num = cur_board[next_x][next_y][0]
            cur_board[next_x][next_y][0] = -1
            cur_ans += fish_num

            move_shark(cur_board, cur_ans)

            cur_board[next_x][next_y][0] = fish_num
            cur_ans -= fish_num

        next_x += dx[di]
        next_y += dy[di]
    if not is_eat:
        ans_list.append(ans)
    return


dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

board = []  # 1~16: 물고기 / 0: 빈칸 / -1: 상어
ans = 0
ans_list = []
for i in range(4):
    temp = []
    row = list(map(int, input().split()))
    for j in range(0, 8, 2):
        temp.append([row[j], row[j + 1]])
    board.append(temp)

ans += init_shark()
move_shark(board, ans)

print(max(ans_list))
