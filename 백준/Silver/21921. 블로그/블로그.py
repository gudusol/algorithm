import sys
from collections import defaultdict as dict

input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))

count_dict = dict(int)
left = 0
right = X - 1
temp = sum(visit[:X])

for _ in range(N - X):
    count_dict[temp] += 1
    temp -= visit[left]
    left += 1
    right += 1
    temp += visit[right]
count_dict[temp] += 1
sorted_arr = sorted(count_dict.items(), reverse=True)

num, c = sorted_arr[0]

if num == 0:
    print('SAD')
else:
    print(num)
    print(c)