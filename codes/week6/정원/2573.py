import sys
from collections import deque

input = sys.stdin.readline

height, width = map(int, input().split())

def bfs(x, y):
    visit[y][x] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        nowX, nowY = queue.popleft()
        if field[nowY][nowX+1] >= 1 and visit[nowY][nowX+1] == 0:
            visit[nowY][nowX+1] = 1
            queue.append((nowX+1, nowY))
        if field[nowY+1][nowX] >= 1 and visit[nowY+1][nowX] == 0:
            visit[nowY+1][nowX] = 1
            queue.append((nowX, nowY+1))
        if field[nowY][nowX-1] >= 1 and visit[nowY][nowX-1] == 0:
            visit[nowY][nowX-1] = 1
            queue.append((nowX-1, nowY))
        if field[nowY-1][nowX] >= 1 and visit[nowY-1][nowX] == 0:
            visit[nowY-1][nowX] = 1
            queue.append((nowX, nowY-1))

def meltCal(x, y):
    if x == 0 or y == 0 or x == width-1 or y == height-1:
        return 0
    else:
        nextIce = field[y][x]
        if field[y][x+1] == 0:
            nextIce -= 1
        if field[y][x-1] == 0:
            nextIce -= 1
        if field[y+1][x] == 0:
            nextIce -= 1
        if field[y-1][x] == 0:
            nextIce -= 1
        return max(0, nextIce)


field = []
for _ in range(height):
    field.append(list(map(int, input().split())))

islandCount = 0
year = -1
while islandCount < 2:
    nextField = []
    visit = [[0 for _ in range(width)] for _ in range(height)]
    islandCount = 0
    for y in range(height):
        tempNext = []
        for x in range(width):
            tempNext.append(meltCal(x, y))
            if visit[y][x] == 0 and field[y][x] >= 1:
                islandCount += 1
                bfs(x, y)
        nextField.append(tempNext)
    field = nextField
    year += 1
    if islandCount == 0:
        break
if islandCount > 1:
    print(year)
else:
    print(0)