import heapq

T = int(input())

for _ in range(T):
    K = int(input())
    cost = list(map(int, input().split()))
    heapq.heapify(cost)

    ans = 0
    while len(cost) > 1:
        temp = heapq.heappop(cost)
        temp += heapq.heappop(cost)
        ans += temp
        heapq.heappush(cost, temp)
    print(ans)
