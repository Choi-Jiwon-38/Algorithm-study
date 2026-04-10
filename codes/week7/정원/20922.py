numberListLen, repeatNum = map(int, input().split())
numberList = list(map(int, input().split()))

frontPointer = 0
backPointer = 0

maxLen = 0

numberBag = [0 for _ in range(200001)]

while frontPointer < numberListLen:
    nowFront = numberList[frontPointer] 
    numberBag[nowFront] += 1

    while numberBag[nowFront] == repeatNum+1:
        nowBack = numberList[backPointer] 
        numberBag[nowBack] -= 1
        backPointer += 1

    maxLen = max(maxLen, frontPointer - backPointer + 1)
    frontPointer += 1

print(maxLen)