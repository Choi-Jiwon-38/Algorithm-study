import sys
input = sys.stdin.readline

n, m = map(int, input().split())
used = [False for _ in range(n + 1)]

def backtrack(arr: list[int], used: list[bool]):
    global n, m
    step = len(arr)

    if step == m:
        print(*arr)
        return True

    for i in range(1, n + 1):
        if used[i]:
            continue
        arr.append(i)
        used[i] = True
        backtrack(arr, used)
        arr.pop()
        used[i] = False


for i in range(1, n + 1):
    used[i] = True
    backtrack([i], used)
    used[i] = False
