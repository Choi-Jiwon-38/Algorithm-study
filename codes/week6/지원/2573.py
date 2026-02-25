import sys
from collections import deque
input = sys.stdin.readline

maps = []
n, m = map(int, input().split())
step = -1
dirs = [(1,0), (-1,0), (0,1), (0,-1)]

for _ in range(n):
    maps.append(list(map(int, input().split())))

visited = [[-1 for _ in range(m)] for __ in range(n)]
    
def bfs(y, x):
    visited[y][x] = step
    q = deque([(y, x)])

    while q:
        cy, cx = q.popleft()
        speed = 0

        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx
            
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
        
            if visited[ny][nx] != step and maps[ny][nx] == 0:
                speed += 1 
                
            if visited[ny][nx] != step and maps[ny][nx] != 0:
                visited[ny][nx] = step
                q.append((ny, nx))

        maps[cy][cx] = max(maps[cy][cx] - speed, 0)

flag = False

while sum(sum(row) for row in maps) != 0:
    step += 1
    bfs_count = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0 and visited[i][j] != step:
                if bfs_count == 1:
                    print(step)
                    exit()
                bfs_count += 1
                bfs(i, j)    

print(0)