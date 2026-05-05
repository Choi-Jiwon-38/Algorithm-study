import sys
input = sys.stdin.readline

n = int(input())
costs = []
enabled = [[True for _ in range(n)] for _ in range(n)]
answer = float('inf')

for _ in range(n):
    costs.append(list(map(int, input().split())))

leaf_pos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# y, x에 꽃을 심을 수 있는지 확인하는 함수
def check_can_plant(y: int, x: int, e: list[list[bool]]):
    if y == 0 or y == n - 1 or x == 0 or x == n - 1:
        return False
    
    if not e[y][x]:
        return False

    for dy, dx in leaf_pos:
        ny, nx = y + dy, x + dx

        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            return False

        if not e[ny][nx]:
            return False
    
    return True

# 해당 함수 수행 전에 check_can_plant를 수행할 것
# y, x에 꽃을 심을 때 발생하는 비용을 반환하는 함수
def calculate_plant_cost(y: int, x: int):
    cost = costs[y][x]

    for dy, dx in leaf_pos:
        ny, nx = y + dy, x + dx
        cost +=  costs[ny][nx]
    
    return cost

# 꽃 모양으로 enabled를 업데이트하는 함수 (backtrack 수행 목적)
# 해당 함수 수행 전에 check_can_plant를 수행할 것
def update_enabled_array(y: int, x: int, status: bool, e: list[list[bool]]):
    e[y][x] = status
    
    for dy, dx in leaf_pos:
        ny, nx = y + dy, x + dx
        e[ny][nx] = status

def plant(cy: int, cx: int, curr_cost: int, e: list[list[bool]], step: int):
    global answer

    if step == 3:
        answer = min(answer, curr_cost)
        return

    for y in range(cy, n):
        # @todo: x의 시작 범위 제어가 아직 되지 않음. y는 스킵하지만 x는 부분적으로 중복 검사
        for x in range(n):
            if check_can_plant(y, x, e):
                update_enabled_array(y, x, False, e)
                cost_ = calculate_plant_cost(y, x)
                plant(y, x, curr_cost + cost_, e, step + 1)
                update_enabled_array(y, x, True, e)
    
plant(0, 0, 0, enabled, 0)
print(answer)