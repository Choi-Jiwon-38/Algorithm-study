import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [-1 for _ in range(n)]
mark = -1

for _ in range(m):
    e, s = map(int, input().split())
    graph[s-1].append(e-1)

def bfs(v):
    count = 0
    visited[v] = mark
    q = deque([v])

    while q:
        x = q.popleft()
        count += 1
        for next in graph[x]:
            if visited[next] != mark:
                visited[next] = mark
                q.append(next)
    
    return count

max_count = 0
answer = []

for i in range(n):
    mark = i
    curr_count = bfs(i)

    if curr_count > max_count:
        answer = [i+1]
        max_count = curr_count
    elif curr_count == max_count:
        answer.append(i+1)

answer.sort()
print(*answer)