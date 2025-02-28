def solution(cap, n, deliveries, pickups):
    deliveries_total = sum(deliveries)
    pickups_total = sum(pickups)
    distance = 0
    
    while deliveries_total > 0 or pickups_total > 0:
        if not deliveries:
            distance += len(pickups)
        elif not pickups:
            distance += len(deliveries)
        else:
            distance += max(len(deliveries), len(pickups))

        delivery_cap = min(deliveries_total, cap)
        deliveries_total -= delivery_cap
        
        while delivery_cap > 0:
            val = min(delivery_cap, deliveries[-1])
            deliveries[-1] -= val
            delivery_cap -= val
            while deliveries and deliveries[-1] == 0:
                deliveries.pop()
    
        pickup_cap = min(pickups_total, cap)
        pickups_total -= pickup_cap
        
        while pickup_cap > 0:
            val = min(pickup_cap, pickups[-1])
            pickups[-1] -= val
            pickup_cap -= val
            while pickups and pickups[-1] == 0:
                pickups.pop()
    return distance * 2