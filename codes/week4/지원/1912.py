import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n
nums = list(map(int, input().split()))

# base case
dp[0] = nums[0]

# recursive case
for i in range(1, n):
    dp[i] = nums[i] + max(dp[i-1], 0)

print(max(dp))