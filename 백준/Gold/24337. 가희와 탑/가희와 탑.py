import sys

input = sys.stdin.readline

n, a, b = map(int, input().split())

if n + 1 < a + b:
    print(-1)
else:
    a_list = [i for i in range(1, a + 1)]
    b_list = [i for i in range(b, 0, -1)]

    if a_list[-1] >= b_list[0]:
        b_list.pop(0)
    else:
        a_list.pop()

    add_list = [1 for _ in range(n - len(a_list) - len(b_list))]

    if len(a_list) == 0:
        b_list = [b_list[0]] + add_list + b_list[1:]
    else:
        a_list = add_list + a_list
    building = a_list + b_list

    print(*building)
