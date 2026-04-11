numLen = int(input())
numList = list(map(int, input().split()))

sumList = []
comulativeSum = 0

for i in numList:
    comulativeSum += i
    sumList.append(comulativeSum)
    
    if comulativeSum <= 0:
        comulativeSum = 0

print(max(sumList))