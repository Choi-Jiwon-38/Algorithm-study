import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tl = []

for _ in range(n):
    tl.append(int(input()))

s = 1
e = m * max(tl)

answer = None

def can_complete(time: int) -> bool:
    global m
    cnt = 0
    for t in tl:
        cnt += time // t
    
    return cnt >= m

def binary_search():
    global s, e, answer
    
    while s <= e:
        m = (s + e) // 2

        if can_complete(m):
            answer = m
            e = m - 1
        else:
            s = m + 1

binary_search()
print(answer)
