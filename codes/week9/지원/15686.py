import sys
input = sys.stdin.readline

city = []

n, m = map(int, input().split())

homes = [] # 집 좌표
chickens = [] # 치킨집 좌표
opened = [] # 치킨집 운영 여부
answer = float('inf')

for y in range(n):
    cols = list(map(int, input().split()))

    for x in range(n):
        if cols[x] == 2:
            chickens.append((y, x))
            opened.append(True)
        elif cols[x] == 1:
            homes.append((y, x))

    city.append(cols)

# 치킨 거리 계산
def calculate_chicken_dist(opened: list[bool]) -> int:
    chicken_dist = 0

    for hy, hx in homes:
        min_dist = float('inf')

        for i in range(len(chickens)):
            if not opened[i]:
                continue 
            cy, cx = chickens[i]
            curr_dist = abs(hy - cy) + abs(hx - cx)
            min_dist = min(min_dist, curr_dist)

        chicken_dist += min_dist
    
    return chicken_dist

def fire(opened: list[bool], start: int, count: int):
    global answer

    if count == len(chickens) - m:
        answer = min(answer, calculate_chicken_dist(opened))
        return
    
    for i in range(start, len(chickens)):       
        opened[i] = False
        fire(opened, i + 1, count + 1)
        opened[i] = True

fire(opened, 0, 0)
print(answer)