import sys
from collections import deque
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

box_info = []

for _ in range(m):
    start, end, num = map(int, input().split())
    box_info.append((end, start, num))

box_info = deque(sorted(box_info))
answer = 0
inventory = [c] * n

for i in range(1, n + 1):
    while len(box_info) and box_info[0][0] == i:
        end, start, num = box_info.popleft()
        can_carry = min(min(inventory[start-1:end-1]), num)

        for j in range(start-1, end-1):
            inventory[j] -= can_carry

        answer += can_carry

print(answer)