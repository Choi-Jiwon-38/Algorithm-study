import sys

input = sys.stdin.readline

vilNum, truckStorage = map(int, input().split())
sendBoxNum = int(input())
boxInfo = []
for i in range(sendBoxNum):
    startVil, endVil, sendBoxNum = map(int, input().split())
    boxInfo.append((startVil, endVil, sendBoxNum))
boxInfo.sort(key=lambda x: x[1])

result = 0

arr = [truckStorage for _ in range(vilNum + 1)]
for x, y, num in boxInfo:
    num = min(num, min(arr[x:y]))
    if num != 0:
        for i in range(x, y):
            arr[i] -= num
        result += num

print(result)