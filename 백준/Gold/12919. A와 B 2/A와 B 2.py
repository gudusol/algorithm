import sys

input = sys.stdin.readline


def dfs(current, cur_len, is_reverse):
    global T, T_len, is_possible

    if current not in T and current not in T[::-1]:
        return

    if cur_len == T_len:
        if is_reverse:
            if T == current[::-1]:
                is_possible = True
        else:
            if T == current:
                is_possible = True
        return

    if is_reverse:
        dfs("A" + current, cur_len + 1, is_reverse)
        dfs("B" + current, cur_len + 1, not is_reverse)
    else:
        dfs(current + "A", cur_len + 1, is_reverse)
        dfs(current + "B", cur_len + 1, not is_reverse)


S = input().strip()
T = input().strip()
T_len = len(T)

is_possible = False

dfs(S, len(S), False)

print(1 if is_possible else 0)
