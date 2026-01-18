towerNum = int(input())

towerList = list(map(int, input().split()))
sendableList = [0]
highestTowerList = [[0, 1000000000]] #Place, Height

for i in range(1, towerNum):
    if towerList[i-1] >= towerList[i]:
        tlNum = len(highestTowerList)
        #print(tlNum, highestTowerList[tlNum-1][1])
        while towerList[i-1] >= highestTowerList[tlNum-1][1]:
            highestTowerList.pop()
            tlNum -= 1
        highestTowerList.append([i, towerList[i-1]])
        sendableList.append(highestTowerList[tlNum][0])
    else:
        tlNum = len(highestTowerList)
        while towerList[i] > highestTowerList[tlNum-1][1]:
            highestTowerList.pop()
            tlNum -= 1
        sendableList.append(highestTowerList[tlNum-1][0])
        

print(*sendableList)