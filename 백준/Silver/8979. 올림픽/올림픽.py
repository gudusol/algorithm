import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ranking = []

for _ in range(N):
    idx, gold, silver, bronze = map(int, input().split())
    ranking.append([gold, silver, bronze, idx])
ranking.sort(reverse=True)

target_idx = 0
while ranking[target_idx][3] != K:
    target_idx += 1

while target_idx > 0:
    cur_g, cur_s, cur_b, cur_idx = ranking[target_idx]
    prev_g, prev_s, prev_b, preb_idx = ranking[target_idx - 1]

    if cur_g == prev_g and cur_s == prev_s and cur_b == prev_b:
        target_idx -= 1
    else:
        break
print(target_idx + 1)
