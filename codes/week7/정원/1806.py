numberListLen, sumCutline = map(int, input().split())

numberList = list(map(int, input().split()))

frontPointer = 0
backPointer = 0

minLen = 1000000
nowLen = 1
nowSum = numberList[0]

while True:
    if nowSum >= sumCutline:
        minLen = min(minLen, nowLen)

    if frontPointer == numberListLen - 1 and nowSum <= sumCutline:
        break
    
    if nowSum < sumCutline:
        frontPointer += 1
        nowSum += numberList[frontPointer]
        nowLen += 1
    else:
        nowSum -= numberList[backPointer]
        backPointer += 1
        nowLen -= 1

    
if minLen == 1000000:
    print(0)
else:
    print(minLen)