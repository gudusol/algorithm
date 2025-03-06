from collections import deque

def solution(operations):
    que = deque([])
    
    for operation in operations:
        op, num = operation.split(' ')
        if op == "I":
            que.append(int(num))
        
        elif op == "D":
            if len(que) == 0:
                continue
            que = deque(sorted(list(que)))
            if num == "1":
                que.pop()
            elif num == "-1":
                que.popleft()
                
    que = deque(sorted(list(que)))
    answer = []
    if len(que) == 0:
        answer = [0, 0]
    elif len(que) == 1:
        answer = [que[0], que[0]]
    else:
        answer = [que.pop(), que.popleft()]
    return answer