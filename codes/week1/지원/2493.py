import sys
input = sys.stdin.readline

n = int(input())
ipt = list(map(int, input().rstrip().split(" ")))

stack = []
answer = [0] * n

for i in range(n - 1, -1, -1):
    currHeight = ipt[i]

    while (len(stack) > 0 and stack[-1][1] < currHeight):
        index, height = stack.pop()
        answer[index] = i + 1
        
    stack.append([i, currHeight])
    

print(*answer)