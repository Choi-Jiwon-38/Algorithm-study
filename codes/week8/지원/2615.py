import sys
input = sys.stdin.readline

maps = []

dirs = [
    (-1, 1), # 대각선(오른쪽 위)
    (1, 1), # 대각선(오른쪽 아래)
    (0, 1), # 오른쪽
    (1, 0) # 아래
]

for _ in range(19):
    maps.append(list(map(int, input().split())))

def check_win(y, x, dy, dx, curr, count):
    ny = y + dy
    nx = x + dx

    if ny < 0 or ny >= 19 or nx < 0 or nx >= 19:
        return count

    if maps[ny][nx] != curr:
        return count

    return check_win(ny, nx, dy, dx, curr, count + 1)


for y in range(19):
    for x in range(19):
        curr = maps[y][x]

        if curr != 0:
            for dy, dx in dirs:
                py, px = y - dy, x - dx

                if not (py < 0 or px < 0 or py >= 19 or px >= 19):
                    if maps[py][px] == maps[y][x]:
                        continue # 이 y, x가 시작점이 아닌 경우 continue

                if check_win(y, x, dy, dx, curr, 1) == 5:
                    print(curr)
                    print(y + 1, x + 1)
                    exit()

print(0)