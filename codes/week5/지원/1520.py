import sys
input = sys.stdin.readline
sys.setrecursionlimit(250000)

m, n = map(int, input().split())

maps = []
dp = [[-1] * n for _ in range(m)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(m):
    maps.append(list(map(int, input().split())))

def dfs(y, x, m, n):
    if dp[y][x] != -1:
        return dp[y][x]

    if y == m - 1 and x == n - 1:
        dp[y][x] = 1
        return dp[y][x]

    sum_count = 0
    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        if (ny < 0 or ny >= m or nx < 0 or nx >= n):
            continue

        if maps[y][x] > maps[ny][nx]:
            if dp[ny][nx] != -1:
                sum_count += dp[ny][nx]
            else:
                sum_count += dfs(ny, nx, m, n)

    dp[y][x] = sum_count
    return dp[y][x]

dfs(0, 0, m, n)
print(dp[0][0])