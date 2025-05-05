import sys

input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
shortcut = []  # lower
answer = []

for word in words:
    is_find = False

    li = word.split()
    for i, w in enumerate(li):
        if w[0].lower() not in shortcut:
            shortcut.append(w[0].lower())
            li[i] = "[" + w[0] + "]" + w[1:]
            answer.append(" ".join(li))
            is_find = True
            break

    if not is_find:
        for i, w in enumerate(word):
            if w == ' ':
                continue
            if w.lower() not in shortcut:
                shortcut.append(w.lower())
                answer.append(word[:i] + "[" + w + "]" + word[i + 1 :])
                is_find = True
                break
    
    if not is_find:
        answer.append(word)

for ans in answer:
    print(ans)
