import sys
sys.setrecursionlimit(10**6)

def dfs(X, Y):
    buildNum.append(0)
    if visitField[Y][X] == 0:
        wormList.append(0)
    visitField[Y][X] = 1
    if mapLen-1 != Y and visitField[Y+1][X] != 1 and field[Y+1][X] == 1:
        visitField[Y+1][X] = 1 
        dfs(X, Y+1)
    if 0 != Y and visitField[Y-1][X] != 1 and field[Y-1][X] == 1:
        visitField[Y-1][X] = 1
        dfs(X, Y-1)
    if mapLen-1 != X and visitField[Y][X+1] != 1 and field[Y][X+1] == 1:
        visitField[Y][X+1] = 1
        dfs(X+1, Y)
    if 0 != X and visitField[Y][X-1] != 1 and field[Y][X-1] == 1:
        visitField[Y][X-1] = 1
        dfs(X-1, Y)

field = []
visitField = []
cabbageList = []
wormList = []
buildNumList = []
mapLen = int(input())
visitField = [list(0 for _ in range(mapLen)) for _ in range(mapLen)]

for _ in range(mapLen):
    field.append(list(map(int, (list(input())))))

for i in range(mapLen):
    for j in range(mapLen):
        if field[j][i] == 1:
            buildNum = []
            if visitField[j][i] == 0:
                dfs(i, j)
                buildNumList.append(len(buildNum))
            
buildNumList.sort()

print(len(wormList))
for i in buildNumList:
    print(i)