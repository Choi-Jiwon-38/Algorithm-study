matrixNum = int(input())

matrixList = []
sliceList = []

for i in range(matrixNum):
    x, y = map(int, input().split())

    if i == 0:
        matrixList.append(x)
    matrixList.append(y)

dp = [[0 for _ in range(matrixNum+1)] for _ in range(matrixNum+1)]

for i in range(1, matrixNum):
    for j in range(1, matrixNum):
        if i+j <= matrixNum:
            tempMinList = []
            for k in range(j, j+i):
                tempMinList.append(dp[j][k] + (matrixList[j-1] * matrixList[k] * matrixList[j+i]) + dp[k+1][j+i])
            dp[j][j+i] = min(tempMinList)

print(dp[1][matrixNum])