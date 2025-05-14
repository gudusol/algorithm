import sys

input = sys.stdin.readline
while True:
    s = input().strip()
    if s == "end":
        break
    lines = [
        s[0:3],
        s[3:6],
        s[6:9],
        s[0] + s[3] + s[6],
        s[1] + s[4] + s[7],
        s[2] + s[5] + s[8],
        s[0] + s[4] + s[8],
        s[2] + s[4] + s[6],
    ]
    x, o = s.count("X"), s.count("O")

    if o > x:
        print("invalid")
    elif x > 5 or o > 4:
        print("invalid")
    elif abs(x - o) >= 2:
        print("invalid")
    elif "OOO" in lines and x > o:
        print("invalid")
    elif "XXX" in lines and x == o:
        print("invalid")
    elif "OOO" not in lines and "XXX" not in lines and "." in s:
        print("invalid")
    else:
        print("valid")
