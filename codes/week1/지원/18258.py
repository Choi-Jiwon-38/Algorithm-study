import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    cmd = input().rstrip()

    if cmd.startswith('push'):
        _, numStr = cmd.split(" ")
        q.append(int(numStr))
    elif cmd == 'pop':
        print(q.popleft() if len(q) != 0 else -1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'front':
        print(q[0] if len(q) != 0 else -1)
    elif cmd == 'back':
        print(q[-1] if len(q) != 0 else -1)
    elif cmd == 'empty':
        print(0 if len(q) else 1)
