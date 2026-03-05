import sys
input = sys.stdin.readline

x, n = map(int, input().split())
visitors = list(map(int, input().split()))

i, j = 0, n-1
max_vistior = curr_visitor = sum(visitors[:n])
count = 1

while j < x - 1:
    curr_visitor -= visitors[i]
    curr_visitor += visitors[j+1]
    i += 1
    j += 1

    if curr_visitor > max_vistior:
        max_vistior = curr_visitor
        count = 1
    elif curr_visitor == max_vistior:
        count += 1

if max_vistior == 0:
    print("SAD")
else:
    print(max_vistior)
    print(count)