import heapq
import math

def get_fare (n, routes, start, end):
    heap = [[0, start]]
    distance = [math.inf for _ in range(n + 1)]
    distance[start] = 0
    
    is_find = False
    
    while len(heap) > 0:
        cur_dis, cur_num = heapq.heappop(heap)
        for next_num, dis in routes[cur_num]:
            next_dis = cur_dis + dis
            if distance[next_num] > next_dis:
                heapq.heappush(heap, [next_dis, next_num])
                distance[next_num] = next_dis
    return distance[end]
    
def solution(n, s, a, b, fares):
    answer = math.inf
    routes = {i: [] for i in range(1, n + 1)}
    for c, d, f in fares:
        routes[c].append([d, f])
        routes[d].append([c, f])
        
    for i in range(1, n + 1):
        temp = 0
        temp += get_fare(n, routes, s, i)
        temp += get_fare(n, routes, i, a)
        temp += get_fare(n, routes, i, b)
        answer = min(answer, temp)
    return answer