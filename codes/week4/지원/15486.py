import sys
input = sys.stdin.readline

n = int(input())
schedules = [None] * n
dp = [0] * (n + 1) # dp[i] <- i - 1일까지 일했을 때 얻을 수 있는 수익

for i in range(n):
    t, p = map(int, input().split())
    schedules[i] = (t, p)

for i in range(n+1):
    dp[i] = max(dp[i], dp[i-1])

    if n == i:
        break
    
    t, p = schedules[i]

    if i + t > n:
        continue

    dp[i + t] = max(dp[i + t], dp[i] + p)

print(dp[n])