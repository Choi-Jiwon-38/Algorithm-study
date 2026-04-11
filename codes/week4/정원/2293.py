import sys

input = sys.stdin.readline

coinTypeNum, targetValue = map(int, input().split())
coinTypeList = []
coinCaseNumList = [0 for _ in range(targetValue+1)]

for _ in range(coinTypeNum):
    coinValue = int(input())
    if coinValue <= targetValue:
        coinTypeList.append(coinValue)

for i in coinTypeList:
    coinCaseNumList[i] += 1
    for j in range(i, len(coinCaseNumList)):
        coinCaseNumList[j] += coinCaseNumList[j-i]


print(coinCaseNumList[-1])