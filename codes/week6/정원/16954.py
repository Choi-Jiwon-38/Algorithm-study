import copy

field = []

dx = [0, 1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

able = 0
def dfs(x, y, deep):
    if y <= deep:
        global able
        able = 1
    else:
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < 8 and ny >= 0 and ny < 8:
                if field[deep][ny][nx] == '.':
                    dfs(nx, ny, deep+1)


for _ in range(8):
    field.append(list(input()))

field = [field]

for i in range(6, -1, -1):
    for j in range(8):
        if field[0][i][j] == "#":
            field[0][i+1][j] = "#"

for i in range(1, 8):
    field.append(copy.deepcopy(field[i-1]))
    field[i].pop()
    field[i].insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])

dfs(0, 7, 0)
print(able)