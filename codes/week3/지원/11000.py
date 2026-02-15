import sys
import heapq
input = sys.stdin.readline

n = int(input())
lectures = []

for _ in range(n):
    s, t = map(int, input().split())
    lectures.append((s, t))

lectures.sort(key=lambda x: (x[0], x[1]))

rooms = []

for lecture_start, lecture_end in lectures:
    if len(rooms):
        if rooms[0] > lecture_start:
            heapq.heappush(rooms, lecture_end)
        else:
            heapq.heappushpop(rooms, lecture_end)
    else:
        heapq.heappush(rooms, lecture_end)

print(len(rooms))