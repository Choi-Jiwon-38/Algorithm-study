import sys
input = sys.stdin.readline

n = int(input())
eggs_s = []
eggs_w = []

for _ in range(n):
    s, w = map(int, input().split())
    eggs_s.append(s)
    eggs_w.append(w)

answer = 0


def hit_egg(i, j):
    eggs_s[i] -= eggs_w[j]
    eggs_s[j] -= eggs_w[i]

    
def revert_hit_egg(i, j):
    eggs_s[i] += eggs_w[j]
    eggs_s[j] += eggs_w[i]


def break_egg(i = 0):
    if i == n:
        update_max_breaked_eggs()
        return

    holded_egg_s = eggs_s[i]

    # 손에 든 계란이 깨져있으면 아무것도 치지 않으므로 continue
    if holded_egg_s <= 0:
        break_egg(i + 1)
    else:
        for j in range(n):
            if i == j:
                continue # 든 계란
        
            if  eggs_s[j] <= 0:
                break_egg(i + 1)
            else:
                hit_egg(i, j)
                break_egg(i + 1)
                revert_hit_egg(i, j)

def update_max_breaked_eggs():
    global answer
    count = 0
    for s in eggs_s:
        if s <= 0:
            count += 1
    
    answer = max(answer, count)

break_egg()
print(answer)