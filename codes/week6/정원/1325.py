import sys
from collections import deque

input = sys.stdin.readline
pcNum, trustNum = map(int, input().split())

def bfs(start):
    visited = [False for _ in range(pcNum+1)]
    queue = deque()
    queue.append(start)
    visited[start] = True
    cnt = 1
    while queue:
        next = queue.popleft()
        for nextPc in pcTrustList[next]:
            if visited[nextPc] == False:
                queue.append(nextPc)
                visited[nextPc] = True
                cnt += 1
    return cnt


pcTrustList = [list() for _ in range(pcNum+1)]  

for i in range(trustNum):
    endPc, startPc = map(int, input().split())
    pcTrustList[startPc].append(endPc)

sumHack = [0]

for i in range(1, pcNum+1):
    sumHack.append(bfs(i))

hackPc = []
maxHack = 0
for i in range(1, pcNum+1):
    if maxHack < sumHack[i]:
        maxHack = sumHack[i]
        hackPc = [i]
    elif maxHack == sumHack[i]:
        hackPc.append(i)

print(*hackPc) 