import sys

input = sys.stdin.readline

p, m = map(int, input().split())
players = []
rooms = []

for _ in range(p):
    player = input().strip().split()
    players.append([int(player[0]), player[1]])

for player in players:
    level, id = player
    is_find = False

    for r in rooms:
        if r["count"] < m and abs(r["level"] - level) <= 10:
            r["count"] += 1
            r["ids"].append([str(level), id])
            is_find = True
            break

    if not is_find:
        rooms.append({"level": level, "count": 1, "ids": [[str(level), id]]})

for r in rooms:
    if r["count"] == m:
        print("Started!")
    else:
        print("Waiting!")
    p_list = r["ids"]
    p_list = sorted(p_list, key=lambda x: x[1])
    for i in p_list:
        print(' '.join(i))
