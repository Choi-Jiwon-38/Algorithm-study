numList = [1 for _ in range(10)]
sumNumList = [10]
for _ in range(1000):
    for i in range(1, 10):
        numList[i] += numList[i-1]
    sumNumList.append(sum(numList))

caseNum = int(input())

for _ in range(caseNum):
    print(sumNumList[int(input())-1])