import math

def solution(progresses, speeds):
    days = []
    answer = []
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    count = 1
    temp = days[0]
    for i in range(1, len(days)):
        if temp >= days[i]:
            count += 1
            if i == len(days) - 1:
                answer.append(count)
            continue
        else:
            answer.append(count)
            count = 1
            temp = days[i]
            if i == len(days) - 1:
                answer.append(count)

    return answer