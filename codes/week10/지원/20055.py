import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

a = deque(list(map(int, input().split())))
robots = []

k_count = 0
step = 0

def step1():
    # 벨트 한 칸 회전
    a.appendleft(a.pop())

    # 로봇도 한 칸 회전 반영
    will_remove = None # 중요: 바로 삭제할 시, for문이 망가질 수 있음.

    for i in range(len(robots)):
        next = (robots[i] + 1) % (2 * n)
        robots[i] = next
    
        if next == n - 1:
            will_remove = robots[i]
    
    if will_remove:
        robots.remove(will_remove)
    


def step2():
    global k_count
    will_remove = None

    for i in range(len(robots)):
        next = (robots[i] + 1) % (2 * n)
        
        # 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상인 경우
        if not next in robots and a[next] > 0:
            robots[i] = next # 로봇을 다음 칸으로 이동
            a[next] -= 1 # 해당 칸 내구도 1 감소

            if a[next] == 0:
                k_count += 1

            # 내리는 위치에 도달하면 내림
            if robots[i] == n - 1: 
                will_remove = robots[i]
    
    if will_remove:
        robots.remove(will_remove)
    

def step3():
    global k_count

    if a[0] > 0:
        robots.append(0)
        a[0] -= 1
        
        if a[0] == 0:
            k_count += 1

def step4():
    global step
    global k_count

    if k_count >= k:
        print(step)
        exit()


while True:
    step += 1
    step1()
    step2()
    step3()
    step4()