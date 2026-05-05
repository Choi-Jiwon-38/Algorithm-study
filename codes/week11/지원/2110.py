import sys
input = sys.stdin.readline

n, c = map(int, input().split())
x = []
answer = None

for _ in range(n):
    x.append(int(input()))

x.sort()

s = 1
e = x[-1]

def can_select(dist: int):
    global n, c
    count = 1
    prev = x[0]

    for i in range(1, n):
        if x[i] - prev >= dist:
            count += 1
            prev = x[i]

    return count >= c
    

def binary_search():
    global s, e, answer
    while s <= e:
        m = (s + e) // 2
        
        if can_select(m):
            s = m + 1
            answer = m
        else:
            e = m - 1

binary_search()
print(answer)
