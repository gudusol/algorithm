N = int(input())
pos_num = []
zero = []
neg_num = []
used = [False] * N

for _ in range(N):
    n = int(input())
    if n > 0:
        pos_num.append(n)
    elif n == 0:
        zero.append(n)
    else:
        neg_num.append(n)

pos_num.sort(reverse=True)
neg_num.sort()
num = pos_num + neg_num + zero

ans = 0
for i in range(len(num) - 1):
    if used[i]:
        continue

    cur_num, next_num = num[i], num[i + 1]
    if (cur_num == 1 or next_num == 1) and cur_num * next_num > 0:
        ans += cur_num
        used[i] = True
        continue
    if cur_num < 0 and next_num == 0:
        used[i] = True
        used[i + 1] = True
        continue
    if cur_num * next_num > 0:
        ans += cur_num * next_num
        used[i] = True
        used[i + 1] = True
    else:
        ans += cur_num
        used[i] = True

if not used[-1]:
    ans += num[-1]
print(ans)
