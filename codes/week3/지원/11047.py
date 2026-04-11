import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

answer = 0

for i in range(n - 1, -1, -1):
    if k == 0:
        break

    if coins[i] > k:
        continue

    answer += k // coins[i]

    k %= coins[i]

print(answer)