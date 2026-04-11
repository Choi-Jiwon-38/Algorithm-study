import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(x, y):
    nowNum = field[y][x]
    
    tempRouteNum = 0
    
    if x != 1 or y != 1:
        if nowNum < field[y+1][x]:
            if routeField[y+1][x] == -1:
                dfs(x, y+1)
            tempRouteNum += routeField[y+1][x]
        if nowNum < field[y][x+1]:
            if routeField[y][x+1] == -1:
                dfs(x+1, y)
            tempRouteNum += routeField[y][x+1]
        if nowNum < field[y-1][x]:
            if routeField[y-1][x] == -1:
                dfs(x, y-1)
            tempRouteNum += routeField[y-1][x]
        if nowNum < field[y][x-1]:
            if routeField[y][x-1] == -1:
                dfs(x-1, y)
            tempRouteNum += routeField[y][x-1]

        routeField[y][x] = tempRouteNum
    else:
        routeField[y][x] = 1
    


y, x = map(int, input().split())

routeField = [[-1 for _ in range(x+2)] for _ in range(y+2)]

field = []
field.append([0 for _ in range(x+2)])
for _ in range(y):
    tempField = [0] + list(map(int, input().split())) + [0]
    field.append(tempField)
field.append([0 for _ in range(x+2)])

dfs(x, y)

print(routeField[y][x])