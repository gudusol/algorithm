import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    n, k, t, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    teams = {i: [0, 0, 0] for i in range(1, n + 1)}
    problems = {i: {j: [] for j in range(1, k + 1)} for i in range(1, n + 1)}

    time = 1
    for i, j, s in data:
        problems[i][j].append(s)
        teams[i][1] += 1
        teams[i][2] = time
        time += 1
    for id in problems:
        for p in problems[id]:
            teams[id][0] += max(problems[id][p]) if len(problems[id][p]) > 0 else 0

    sorted_teams = sorted(teams.items(), key=lambda x: (-x[1][0], x[1][1], x[1][2]))

    for team_idx in range(len(sorted_teams)):
        if sorted_teams[team_idx][0] == t:
            print(team_idx + 1)
            break