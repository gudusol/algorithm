import sys
input = sys.stdin.readline

M = int(input())
s = 0


for _ in range(M):
    command = ""
    value = 0
    line = input().split()
    if line[0] == "all" or line[0] == "empty":
        command = line[0]
    else:
        command = line[0]
        value = int(line[1])

    if command == "add":
        s |= 1 << value
    elif command == "remove":
        s &= ~(1 << value)
    elif command == "check":
        if s & (1 << value):
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if s & (1 << value):
            s &= ~(1 << value)
        else:
            s |= 1 << value
    elif command == "all":
        s = (1 << 21) - 1
    elif command == "empty":
        s = 0
