from collections import deque

def solution(priorities, location):
    queue = deque([(i, priorities[i]) for i in range(len(priorities))])
    answer = []
    while len(queue) > 0:
        temp = queue.popleft()
        flag = True
        
        for idx, value in queue:
            if value > temp[1]:
                queue.append(temp)
                flag = False
                break
        
        if flag:
            answer.append(temp)

    for i in range(len(answer)):
        idx, value = answer[i]
        if idx == location:
            return i + 1
