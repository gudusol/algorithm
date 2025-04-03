import sys

input = sys.stdin.readline

N, type = input().strip().split()
max_player = 0
if type == "Y":
    max_player = 2
elif type == "F":
    max_player = 3
elif type == "O":
    max_player = 4

player = set()

for _ in range(int(N)):
    player.add(input().strip())

print(len(player) // (max_player - 1))
