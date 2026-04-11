rockNum = int(input())
rockJumpList = []

for _ in range(rockNum-1):
    smallJump, bigJump = map(int, input().split())
    rockJumpList.append([smallJump, bigJump])
hugeJumpCost = int(input())

optimizeEnergyList = [0]
jumpOptimizeEnergyList = [0, 10**10, 10**10]

if rockNum == 1:
    print(0)
elif rockNum == 2:
    print(rockJumpList[0][0])
elif rockNum == 3:
    print(min(rockJumpList[0][0] + rockJumpList[1][0], rockJumpList[0][1]))
else:
    optimizeEnergyList.append(rockJumpList[0][0])
    optimizeEnergyList.append(min(rockJumpList[0][0] + rockJumpList[1][0], rockJumpList[0][1]))
    jumpOptimizeEnergyList.append(hugeJumpCost)
    for i in range(3, rockNum):
        optimizeEnergyList.append(min(optimizeEnergyList[i-2] + rockJumpList[i-2][1], optimizeEnergyList[i-1] + rockJumpList[i-1][0]))
        if i > 3:
            jumpOptimizeEnergyList.append(min(jumpOptimizeEnergyList[i-2] + rockJumpList[i-2][1], jumpOptimizeEnergyList[i-1] + rockJumpList[i-1][0], optimizeEnergyList[i-3] + hugeJumpCost))

    print(min(optimizeEnergyList[-1], jumpOptimizeEnergyList[-1]))
