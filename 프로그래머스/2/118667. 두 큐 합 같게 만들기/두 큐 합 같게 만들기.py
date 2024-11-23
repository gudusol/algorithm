def solution(queue1, queue2):
    
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    
    sum12 = sum_1 + sum_2
    
    if sum12 % 2 != 0:
        return -1
    target = sum12 // 2

    que = queue1 + queue2
    cur = sum_1
    queue_len = len(queue1)

    pop_idx = 0
    push_idx = queue_len
    
    
    for i in range(3 * queue_len):
        if cur == target:
            return i
        elif cur > target:
            cur -= que[pop_idx]
            pop_idx += 1
            if pop_idx >= 2 * queue_len:
                pop_idx = 0
        elif cur < target:
            cur += que[push_idx]
            push_idx += 1
            if push_idx >= 2 * queue_len:
                push_idx = 0

    return -1