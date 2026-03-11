import sys

input = sys.stdin.readline

dayNum = int(input())
counselList = []

for _ in range(dayNum):
    day, cost = map(int, input().split())
    counselList.append([day, cost])

costList = [0 for _ in range(dayNum+1)]

for i in range(dayNum):
    afterDay = i + counselList[i][0]
    
    costList[i] = max(costList[i-1], costList[i])

    if afterDay <= dayNum:
        costList[afterDay] = max(counselList[i][1], costList[i] + counselList[i][1], costList[afterDay])
    
print(max(costList))