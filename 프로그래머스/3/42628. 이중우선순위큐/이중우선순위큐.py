import heapq as hq

def solution(operations):
    min_heap = []
    max_heap = []
    for operation in operations:
        op, num = operation.split(" ")
        num = int(num)
        
        if op == "I":
            hq.heappush(min_heap, num)
            hq.heappush(max_heap, - num)
        elif op == "D":
            if len(min_heap) == 0:
                continue
            
            if num == 1:
                hq.heappop(max_heap)
                min_heap = []
                for i in max_heap:
                    hq.heappush(min_heap, -i)
            elif num == -1:
                hq.heappop(min_heap)
                max_heap = []
                for i in min_heap:
                    hq.heappush(max_heap, -i)
    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [- hq.heappop(max_heap), hq.heappop(min_heap)]
        