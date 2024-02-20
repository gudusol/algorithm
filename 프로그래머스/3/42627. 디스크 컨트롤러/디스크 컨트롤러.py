import heapq as hq

def solution(jobs):
    hq.heapify(jobs) # 시작시간 오름차순
    count = len(jobs)
    answer = 0
    t = 0
    tasks = [] # 소요시간 오름차순
    while len(jobs) > 0 or len(tasks) > 0:
        while len(jobs) > 0:
            start, time = hq.heappop(jobs)
            if (t >= start):
                hq.heappush(tasks, [time, start]) # 소요시간 짧은 순
            else:
                hq.heappush(jobs, [start, time]) 
                break
        
        if len(tasks) > 0 :
            time, start = hq.heappop(tasks)
            t += time
            answer += (t - start)     
        else:
            start, time = hq.heappop(jobs)
            t = start + time
            answer += (t - start)     
    
    return answer // count