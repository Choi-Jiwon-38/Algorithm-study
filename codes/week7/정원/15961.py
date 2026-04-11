import sys
input = sys.stdin.readline

dishNum, varietyOfSushi, chainNum, coupon = map(int, input().split())

sushiList = []

for _ in range(dishNum):
    tempDish = int(input())
    sushiList.append(tempDish)

sushiList = sushiList + sushiList[:-1]

nowVarietyOfSushiNum = 0
maxVarietyOfSushiNum = 0

frontDish = chainNum - 1
backDish = 0

nowDishStatus = [0 for _ in range(varietyOfSushi+1)]

for i in range(chainNum):
    if nowDishStatus[sushiList[i]] == 0:
        nowVarietyOfSushiNum += 1

    nowDishStatus[sushiList[i]] += 1

maxVarietyOfSushiNum = max(maxVarietyOfSushiNum, nowVarietyOfSushiNum)

while frontDish != len(sushiList) - 1:
    frontDish += 1
    if nowDishStatus[sushiList[frontDish]] == 0:
        nowVarietyOfSushiNum += 1

    nowDishStatus[sushiList[frontDish]] += 1


    nowDishStatus[sushiList[backDish]] -= 1

    if nowDishStatus[sushiList[backDish]] == 0:
        nowVarietyOfSushiNum -= 1

    backDish += 1
    
    if nowDishStatus[coupon] == 0:
        maxVarietyOfSushiNum = max(maxVarietyOfSushiNum, nowVarietyOfSushiNum+1)
    else:
        maxVarietyOfSushiNum = max(maxVarietyOfSushiNum, nowVarietyOfSushiNum)

print(maxVarietyOfSushiNum)