import sys

input = sys.stdin.readline

num = input().strip()

string = ''
string_idx = 0
idx = 0
answer = 0

while idx < len(num):
    answer += 1
    string += str(answer)
    while string_idx < len(string) and idx < len(num):
        if num[idx] == string[string_idx]:
            idx += 1
        string_idx += 1

print(answer)