import sys
input = sys.stdin.readline

n = int(input())
matrixs = [None for _ in range(n+1)]

# dp[i][j]는 행렬 i부터 행렬 j까지 곱에 필요한 곱셈의 횟수
# dp[i][j] => dp[i][k] + dp[k+1][j] + i * j * k
dp = [[0 for _ in range(n+1)] for __ in range(n+1)]

for i in range(n):
    r, c = map(int, input().split())
    matrixs[i], matrixs[i + 1] = r, c
    
def minimum(i, j):
    cnt = float('inf')
    
    for k in range(i, j):
        curr_result = dp[i][k] + dp[k+1][j] + matrixs[i - 1] * matrixs[k] * matrixs[j]
        if cnt > curr_result: cnt = curr_result
    
    return cnt

for length in range(1, n): # length = j - i
    for i in range(1, n - length + 1): 
        j = i + length
        dp[i][j] = minimum(i, j)

print(dp[1][n])
