import sys 

commandNum = int(input())
stackList = []

for i in range(commandNum):
    command = list(sys.stdin.readline().split())

    if len(command) == 2:
        command[1] = int(command[1])

    if command[0] == "push":
        stackList.append(command[1])
    elif command[0] == "pop":
        if len(stackList) != 0:
            print(stackList.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stackList))
    elif command[0] == "empty":
        if len(stackList) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "top":
        if len(stackList) != 0:
            print(stackList[-1])
        else:
            print(-1)