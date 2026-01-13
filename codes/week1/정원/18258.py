import sys

commandNum = int(input())
queue = []

#deque를 사용하지 않고 풀어보기 위해 새로운 방법 도입
queueNum = 0

for i in range(commandNum):
    inputList = sys.stdin.readline().split()
    if len(inputList) == 2:
        inputList[1] = int(inputList[1])

    if inputList[0] == 'push':
        queue.append(inputList[1])

    elif inputList[0] == 'pop':
        if queueNum < len(queue):
            print(queue[queueNum])
            queueNum += 1
        else:
            print(-1)

    elif inputList[0] == 'size':
        print(len(queue)-queueNum)

    elif inputList[0] == 'empty':
        if queueNum == len(queue):
            print(1)
        else:
            print(0)

    elif inputList[0] == 'front':
        if queueNum == len(queue):
            print(-1)
        else:
            print(queue[queueNum])
    
    elif inputList[0] == 'back':
        if queueNum == len(queue):
            print(-1)
        else:
            print(queue[-1])