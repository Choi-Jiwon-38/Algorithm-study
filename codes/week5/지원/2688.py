import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [[1] * 10 for _ in range(n)] 

    for i in range(1, n):
        for j in range(1, 10):
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
    print(sum(dp[n-1]))