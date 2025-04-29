import sys
from collections import Counter

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    count = Counter(numbers)

    team_scores = {i: [] for i in count}
    score = 1

    for n in numbers:
        if count[n] == 6:
            team_scores[n].append(score)
            score += 1

    scores = {}
    for c in count:
        if count[c] == 6:
            scores[c] = sum(team_scores[c][:4])
    min_score = min(scores.values())

    scores.values()

    answer = []
    for num in scores:
        if scores[num] == min_score:
            answer.append([team_scores[num][4], num])

    answer.sort()

    print(answer[0][1])
