import sys
input = sys.stdin.readline

maps = []

h, w = map(int, input().split())
wall = list(map(int, input().split()))

for i in range(h):
    maps.append(['#' if i < wall[j] else '' for j in range(w)])

answer = 0

for i in range(h):
    rain = 0
    flag = False

    for j in range(w):
        if maps[i][j] == '#':
            answer += rain
            rain = 0
            flag = True
        else:
            if flag:
                rain += 1

print(answer)