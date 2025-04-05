import sys

input = sys.stdin.readline

switch_n = int(input())
switch = [False] * (switch_n + 1)
switch_input = list(map(int, input().split()))
for idx, val in enumerate(switch_input):
    switch[idx + 1] = True if val == 1 else False

for _ in range(int(input())):
    gender, num = map(int, input().split())

    if gender == 1:
        idx = num
        while idx <= switch_n:
            switch[idx] = not switch[idx]
            idx += num

    elif gender == 2:
        left, right = num - 1, num + 1
        switch[num] = not switch[num]
        while True:
            if 1 <= left <= switch_n and 1 <= right <= switch_n:
                if switch[left] == switch[right]:
                    switch[left] = not switch[left]
                    switch[right] = not switch[right]
                    left -= 1
                    right += 1
                else:
                    break
            else:
                break

answer_idx = 1
is_end = False
while True:
    for _ in range(20):
        if answer_idx == switch_n:
            print(1 if switch[answer_idx] else 0)
            is_end = True
            break
        else:
            print(1 if switch[answer_idx] else 0, end=" ")
        answer_idx += 1
    if is_end:
        break
    print()
