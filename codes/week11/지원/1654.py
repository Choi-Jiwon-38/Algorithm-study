import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
answer = None

for _ in range(k):
    lines.append(int(input()))

lines.sort()

def cut_line():
    global answer

    s = 0
    e = lines[-1]

    while s <= e:
        m = (s + e) // 2
        count = count_cutted_line(m)

        if count < n:
            e = m - 1
            continue
        else:
            answer = m
            s = m + 1

def count_cutted_line(base):
    base = 1 if base == 0 else base

    count = 0

    for line in lines:
        count += line // base
    
    return count

cut_line()
print(answer)   