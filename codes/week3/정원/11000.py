import sys
import heapq

input = sys.stdin.readline

lessonNum = int(input())
classroomQueue = []
classes = []

for _ in range(lessonNum):
    startTime, endTime = map(int, input().split())
    classes.append([startTime, endTime])

classes.sort()

heapq.heappush(classroomQueue, classes[0][1])

for i in range(1, lessonNum):
    if classes[i][0] >= classroomQueue[0]:
        heapq.heappop(classroomQueue)
    heapq.heappush(classroomQueue, classes[i][1])

print(len(classroomQueue))