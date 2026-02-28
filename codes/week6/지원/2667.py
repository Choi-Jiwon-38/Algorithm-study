import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
maps=[]
answer = []
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(n):
    maps.append(list(map(int, input().strip())))

def bfs(y, x):
    count = 0
    maps[y][x] = 0
    q = deque([(y, x)])

    while q:
        cy, cx = q.popleft()
        count += 1
        for dy, dx in dirs:
            ny = cy + dy
            nx = cx + dx

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
        
            if maps[ny][nx] == 1:
                maps[ny][nx] = 0
                q.append((ny, nx))
    
    return count

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for a in answer:
    print(a)