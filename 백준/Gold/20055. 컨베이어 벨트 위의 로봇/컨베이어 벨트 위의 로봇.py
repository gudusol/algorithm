import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
belt = list(map(int, input().split()))

robot = deque([])
up = 0
down = N - 1

broken = 0

turn = 0

while broken < K:
    turn += 1

    # step1
    up -= 1
    down -= 1
    if up < 0:
        up += 2 * N
    if down < 0:
        down += 2 * N
    if robot and robot[0] == down:
        robot.popleft()

    # step2
    for idx, r in enumerate(robot):
        next = (r + 1) % (2 * N)
        if belt[next] > 0 and next not in robot:
            robot[idx] = (robot[idx] + 1) % (2 * N)
            belt[next] -= 1
            if belt[next] == 0:
                broken += 1

    if robot and robot[0] == down:
        robot.popleft()

    # step3
    if belt[up] > 0:
        robot.append(up)
        belt[up] -= 1
        if belt[up] == 0:
            broken += 1

print(turn)
