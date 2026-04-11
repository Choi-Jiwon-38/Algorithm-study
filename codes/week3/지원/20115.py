import sys
input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

for i in range(n - 1):
    drinks[n - 1] += drinks[i] / 2

print(drinks[n - 1])