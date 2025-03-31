import sys

input = sys.stdin.readline

a_list = ["a", "e", "i", "o", "u"]
while True:
    is_accept = True
    word = input().strip()
    if word == "end":
        break

    count = 0
    repeat = 0
    prev = ""
    is_prve_모음 = False

    for w in word:
        if w != "e" and w != "o":
            if prev == w:
                is_accept = False
                break

        prev = w
        if w in a_list:
            # 모음일때
            count += 1
            if is_prve_모음:
                repeat += 1
            else:
                repeat = 1
            if repeat == 3:
                break
            is_prve_모음 = True

        else:
            # 자음일때
            if not is_prve_모음:
                repeat += 1
            else:
                repeat = 1
            if repeat == 3:
                break
            is_prve_모음 = False

    if count == 0:
        is_accept = False
    if repeat == 3:
        is_accept = False

    if is_accept:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
