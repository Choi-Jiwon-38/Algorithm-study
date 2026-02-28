import sys
from collections import deque
input = sys.stdin.readline

n = 8
maps = deque([])

first_wall_index_r = None

for i in range(n):
    rows = list(input().rstrip())
    
    if first_wall_index_r is None and '#' in rows:
        first_wall_index_r = n - i - 1

    maps.append(rows)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)]

q = deque([(n-1, 0)])

step = 0

while q:
    if first_wall_index_r is None or step > first_wall_index_r:
        print(1)
        exit()
    
    iter_count = len(q)
    
    for i in range(iter_count):
        y, x = q.popleft()

        next_pos = set()

        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx

            # map 밖으로 이동하려는 경우
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            # 이동하려는 곳이 벽인 경우
            if maps[ny][nx] == '#':
                continue

            # 이동한 곳으로 벽이 내려오는 경우
            if ny - 1 >= 0 and maps[ny - 1][nx] == '#':
                continue
        
            if ny == 0 and nx == n - 1: # 도착
                print(1)
                exit()

            next_pos.add((ny, nx))

        for pos in next_pos:
            q.append(pos)

    # 벽을 한 칸 밀어냄
    maps.pop()
    maps.appendleft([0 for _ in range(n)])
    step += 1

print(0)