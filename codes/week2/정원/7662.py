import sys
import heapq

input = sys.stdin.readline

caseNum = int(input())

for _ in range(caseNum):
    maxHeap = []
    minHeap = []
    pushNum, popNum = 0, 0
    cmdNum = int(input())
    isDeleted = [False]*cmdNum
    for i in range(cmdNum):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(minHeap, [num, i])
            heapq.heappush(maxHeap, [-num, i])
            pushNum += 1
        else:
            if num == 1:
                while maxHeap and isDeleted[maxHeap[0][1]]: 
                    heapq.heappop(maxHeap)
                    
                if maxHeap:
                    isDeleted[maxHeap[0][1]] = True
                    heapq.heappop(maxHeap)
                    popNum += 1
                    if pushNum == popNum:
                        maxHeap = []
                        minHeap = []
            else:
                while minHeap and isDeleted[minHeap[0][1]]: 
                    heapq.heappop(minHeap)

                if minHeap: 
                    isDeleted[minHeap[0][1]] = True
                    heapq.heappop(minHeap)
                    popNum += 1
                    if pushNum == popNum:
                        maxHeap = []
                        minHeap = []
                        
    
    while maxHeap and isDeleted[maxHeap[0][1]]: 
        heapq.heappop(maxHeap)
    while minHeap and isDeleted[minHeap[0][1]]: 
        heapq.heappop(minHeap)
    

    if maxHeap: maxQueueNum = -heapq.heappop(maxHeap)[0]
    if minHeap: minQueueNum = heapq.heappop(minHeap)[0]
    
    if pushNum == popNum:
        print("EMPTY")
    else:
        print(maxQueueNum, minQueueNum)