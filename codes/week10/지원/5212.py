import sys
input = sys.stdin.readline

r, c = map(int, input().split())
maps = []
islands = []
survived = []
removed = []

for y in range(r):
    row = list(input().rstrip())

    for x in range(c):
        if row[x] == 'X':
            islands.append((y, x)) 

    maps.append(row)

def will_survive(y, x):
    count = 0
    
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny = y + dy
        nx = x + dx

        if ny < 0 or ny >= r or nx < 0 or nx >= c:
            count += 1
            continue
        
        if maps[ny][nx] == '.':
            count += 1
    
    return False if count >= 3 else True

# 잔존하는 섬에서 잠긴 
for island in islands:
    y, x = island

    if will_survive(y, x):
        survived.append(island)
    else:
        removed.append(island)

# 섬이 하나만 남은 경우, 지도 갱신 및 출력 범위는 수행하기 전에 조기 반환
if len(survived) == 1:
    print('X')
    exit()

# 잠긴 섬을 지도에 갱신
for removed_island in removed:  
    y, x = removed_island
    maps[y][x] = '.'

# 출력해야 하는 범위를 계산
start_y, start_x = survived[0]
end_y, end_x = start_y, start_x

for survived_island in survived:
    y, x = survived_island
    
    start_y = min(y, start_y)
    start_x = min(x, start_x)
    end_y = max(y, end_y)
    end_x = max(x, end_x)

# 출력
for y in range(start_y, end_y + 1):
    for x in range(start_x, end_x + 1):
        print(maps[y][x] , end='')
    print()