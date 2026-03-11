import sys
input = sys.stdin.readline

n = int(input())
dp = [[float('inf')] * 2 for _ in range(n)]
jumps = [None] * (n-1)

dp[0][0] = 0

for i in range(n-1):
    small_jump_cost, large_jump_cost = map(int, input().split())
    jumps[i] = (small_jump_cost, large_jump_cost)

k = int(input())

for i in range(n-1):
    x, y = jumps[i]

    for j in range(2):
        if i + 1 <= n - 1:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + x)

        if i + 2 <= n - 1:
            dp[i + 2][j] = min(dp[i + 2][j], dp[i][j] + y)

        if i + 3 <= n - 1 and j == 0:
            dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + k)

print(min(dp[n-1]))