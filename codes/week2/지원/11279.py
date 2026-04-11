import sys
import heapq
input = sys.stdin.readline

n = int(input())
hq = []

for _ in range(n):
    num = int(input())

    if num == 0:
        print(-heapq.heappop(hq) if len(hq) else 0)
    else:
        heapq.heappush(hq, -num)