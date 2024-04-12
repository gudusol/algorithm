def check_up(runway, idx, check_arr):
    global L

    height = runway[idx - 1]

    for i in range(idx - 1, idx - 1 - L, -1):
        if i < 0 or not check_arr[i] or runway[i] != height:
            return False

    for i in range(idx - 1, idx - 1 - L):
        check_arr[i] = False
    return True


#  뒤쪽 보는거라서 check_arr 확인 안해도 될거같긴한데,,, 맞나?
def check_down(runway, idx, check_arr):
    global N, L

    height = runway[idx]
    for i in range(idx, idx + L):
        if i >= N or runway[i] != height:
            return False

    for i in range(idx, idx + L):
        check_arr[i] = False
    return True


def check_pass(runway):
    global N, L
    check_arr = [True] * N
    prev_h = runway[0]
    idx = 1
    while idx < N:
        next_h = runway[idx]
        if prev_h == next_h:
            idx += 1
            continue
        elif abs(prev_h - next_h) >= 2:
            return False
        elif prev_h + 1 == next_h:
            if check_up(runway, idx, check_arr):
                prev_h = runway[idx]
                idx += 1
            else:
                return False
        elif prev_h - 1 == next_h:
            if check_down(runway, idx, check_arr):
                idx += L
                prev_h = runway[idx - 1]
            else:
                return False
    return True


N, L = map(int, input().split())
runways = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(runways[j][i])
    runways.append(temp)

ans = 0
for runway in runways:
    if check_pass(runway):
        ans += 1
print(ans)
