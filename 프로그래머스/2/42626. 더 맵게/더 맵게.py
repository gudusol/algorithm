import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for value in scoville:
        heapq.heappush(heap, value)
        
    while heap[0] < K:
        if len(heap) < 2:
            return -1
        heapq.heappush(heap, heapq.heappop(heap) + (2 * heapq.heappop(heap)))
        answer += 1
    
    return answer