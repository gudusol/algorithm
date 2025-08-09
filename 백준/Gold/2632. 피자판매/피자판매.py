import sys
from collections import defaultdict

input = sys.stdin.readline

size = int(input())
m, n = map(int, input().split())

M = []
N = []

for _ in range(m):
    M.append(int(input()))
for _ in range(n):
    N.append(int(input()))


def make_list(list):
    len_li = len(list)
    return_dict = defaultdict(int)
    for i in range(len_li):
        temp = 0
        for num in list[i:] + list[:i]:
            temp += num
            if temp > size:
                break
            return_dict[temp] += 1
    return_dict[sum(list)] = 1
    return return_dict


m_dict = make_list(M)
n_dict = make_list(N)
m_dict[0] = 1
n_dict[0] = 1

answer = 0
for i in m_dict.keys():
    if size - i in n_dict:
        answer += m_dict[i] * n_dict[size - i]
print(answer)
