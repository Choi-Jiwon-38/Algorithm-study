import sys
import heapq

input = sys.stdin.readline
unsolvedDict = {}
problemCount = int(input())
minHeap = []
maxHeap = []

for _ in range(problemCount):
    problemNumber, level = map(int, input().split())
    heapq.heappush(minHeap, [level, problemNumber])
    heapq.heappush(maxHeap, [-level, -problemNumber])
    unsolvedDict[problemNumber] = level

cmdCount = int(input())

for _ in range(cmdCount):
    cmdList = input().split()
    if cmdList[0] == "recommend":
        if cmdList[1] == "1":
            while True:
                solveProblemLevel, solveProblemNumber = map(int, maxHeap[0])
                if -solveProblemNumber in unsolvedDict and -solveProblemLevel == unsolvedDict[-solveProblemNumber]:
                    print(-solveProblemNumber)
                    break
                else:
                    heapq.heappop(maxHeap)
        else:
            while True:
                solveProblemLevel, solveProblemNumber = map(int, minHeap[0])
                if solveProblemNumber in unsolvedDict and solveProblemLevel == unsolvedDict[solveProblemNumber]:
                    print(solveProblemNumber)
                    break
                else:
                    heapq.heappop(minHeap)


    elif cmdList[0] == "add":
        problemNumber, level = int(cmdList[1]), int(cmdList[2])
        heapq.heappush(minHeap, [level, problemNumber])
        heapq.heappush(maxHeap, [-level, -problemNumber])
        unsolvedDict[problemNumber] = level

    else:
        del unsolvedDict[int(cmdList[1])]
    