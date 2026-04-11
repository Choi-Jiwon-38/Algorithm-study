import sys

input = sys.stdin.readline

coinTypeNum, money = map(int, input().split())
coinType = []
totalCoinNum = 0

for _ in range(coinTypeNum):
    coinType.append(int(input()))

for i in range(coinTypeNum-1, -1, -1):
    coinValue = coinType[i]

    nowCoinNum = money // coinValue
    totalCoinNum += nowCoinNum
    money -= nowCoinNum * coinValue

print(totalCoinNum)