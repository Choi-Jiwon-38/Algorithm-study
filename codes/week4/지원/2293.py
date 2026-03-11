import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

# base case
dp = [0] * (k + 1)
dp[0] = 1

# recursive case
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin] 

print(dp[k])