import sys
input = sys.stdin.readline

n, m  = map(int, input().split())

maps = [[None] * m for _ in range(n)]
dp = [[None] * m for _ in range(n)] # i, j 번째까지 합


for i in range(n):
    cols = list(map(int, input().split()))

    for j in range(m):
        # map 설정
        maps[i][j] = cols[j]

        if i == 0:
            if j == 0:
                dp[i][j] = maps[i][j]
            else:
                dp[i][j] = maps[i][j] + dp[i][j-1]

        else: # i > 0
            if j == 0:
                dp[i][j] = dp[i-1][j] + maps[i][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] + maps[i][j] - dp[i-1][j-1]

k = int(input())

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    answer = dp[x2-1][y2-1]

    if x1 - 1 > 0 and y1 - 1 > 0:
        answer -= dp[x1-2][y2 -1]
        answer -= dp[x2 - 1][y1- 2]
        answer += dp[x1 - 2][y1- 2]
        
    elif x1 - 1 > 0:
        answer -= dp[x1-2][y2 - 1]
        
    elif y1 - 1 > 0:
        answer -= dp[x2 - 1][y1- 2]
    
    print(answer)