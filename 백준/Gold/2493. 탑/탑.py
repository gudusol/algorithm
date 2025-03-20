import sys

input = sys.stdin.readline

N = int(input())
towers = map(int, input().split())

laser_tower = []

answer = [0] * N

for idx, tower in enumerate(towers):
    while laser_tower and laser_tower[-1][1] < tower:
        laser_tower.pop()

    if laser_tower:
        answer[idx] = laser_tower[-1][0] + 1
    laser_tower.append([idx, tower])

print(*answer)