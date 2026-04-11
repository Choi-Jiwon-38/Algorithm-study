import sys
input = sys.stdin.readline

height, width = map(int, input().split())
mapList = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

for i in range(1, height + 1):
    numberList = list(map(int, input().split()))
    mapList[i][0] = 0
    for j in range(1, width + 1):
        mapList[i][j] = mapList[i][j-1] + mapList[i-1][j] - mapList[i-1][j-1] + numberList[j-1]

questionNum = int(input())

for _ in range(questionNum):
    startY, startX, endY, endX = map(int, input().split())

    print(mapList[endY][endX] - mapList[startY-1][endX] - mapList[endY][startX-1] + mapList[startY-1][startX-1])
