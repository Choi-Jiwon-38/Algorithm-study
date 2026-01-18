import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    ipt = list(input().rstrip().split(" "))

    if len(ipt) == 2:
        q.append(ipt[1])
    else:
        cmd = ipt[0]
        isEmpty = len(q) == 0

        if cmd == 'pop':
            print(-1 if isEmpty else q.pop())
        elif cmd == 'size':
            print(len(q))
        elif cmd == 'top':
            print(-1 if isEmpty else q[-1])
        elif cmd == 'empty':
            print(1 if isEmpty else 0)
