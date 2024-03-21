from collections import deque

def solution(people, limit):
    people.sort()
    q = deque(people)
    count = 0
    while q:
        boat = q.pop()
        if q and boat + q[0] <= limit:
            boat += q.popleft()
        count += 1
    return count
