from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    arrived = []
    time = 0
    sum_weight = 0
    
    while len(arrived) < len(truck_weights):
        arrive_truck = bridge.popleft()
        if arrive_truck != 0:
            arrived.append(arrive_truck)
            sum_weight -= arrive_truck
    
        depart_truck = trucks.popleft() if len(trucks) > 0 else 0
            
        if sum_weight + depart_truck <= weight:
            bridge.append(depart_truck)
            sum_weight += depart_truck
        else:
            trucks.appendleft(depart_truck)
            bridge.append(0)
    
        time += 1
        
    return time