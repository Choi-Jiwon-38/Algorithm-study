import sys
input = sys.stdin.readline

n, m = map(int, input().split())
office = []
cctv_loc = []
cctv_dir = {
    1: [
        [(0, 1)],
        [(0, -1)],
        [(1, 0)],
        [(-1, 0)]
    ],
    2: [
        [(0, 1), (0, -1)],
        [(1, 0), (-1, 0)]
    ],
    3: [
        [(0, 1), (1, 0)],
        [(0, -1), (1, 0)],
        [(0, 1), (-1, 0)],
        [(0, -1), (-1, 0)]
    ],
    4: [
        [(0, -1), (1, 0), (-1, 0)],
        [(0, 1), (1, 0), (-1, 0)],
        [(0, 1), (0, -1), (-1, 0)],
        [(0, 1), (0, -1), (1, 0)]
    ],
    5: [
        [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ],
}

answer = float('inf')

for y in range(n):
    row = list(map(int, input().split()))

    for x in range(m):
        if row[x] > 0 and row[x] < 6:
            cctv_loc.append((y, x))

    office.append(row)

max_step = len(cctv_loc)

def apply(board, y, x, directions):
    changed = []

    for dy, dx in directions:
        ny = y + dy
        nx = x + dx

        while 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 6:
                break
        
            if board[ny][nx] == 0:
                board[ny][nx] = '#'
                changed.append((ny, nx))
            
            ny += dy
            nx += dx
    
    return changed

def rollback(board, changed):
    for y, x in changed:
        board[y][x] = 0

def dfs(office, step = 0):
    global answer
    
    if step == max_step:
        cnt = 0

        for i in range(n):
            for j in range(m):
                if office[i][j] == 0:
                    cnt += 1

        answer = min(answer, cnt)
        return

    y, x = cctv_loc[step]

    directions = cctv_dir[office[y][x]]

    for dirs in directions:
        changed = apply(office, y, x, dirs)
        dfs(office, step + 1)
        rollback(office, changed)

dfs(office)
print(answer)