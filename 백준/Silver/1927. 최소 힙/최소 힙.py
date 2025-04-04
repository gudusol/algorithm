import sys
import heapq

input = sys.stdin.readline

list = []

N = int(input())

for _ in range(N):
    command = int(input())

    if command == 0:
        try:
            print(heapq.heappop(list))
        except:
            print(0)

    elif command > 0:
        heapq.heappush(list, command)
