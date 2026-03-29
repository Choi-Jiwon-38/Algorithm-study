## 문제 풀이 Key Point 및 막혔던 부분

### 죽음의 비 (22944)

- 방문 처리를 어떻게 진행해야 하는지
  1. 처음에는 `visited[y][x] = True | False`와 같은 형태로 관리하였으나, 우산을 획득하고 이미 지나온 경로를 다시 가는 경우가 존재
  2. 1의 문제를 해결하기 위하여 `visited[y][x][0 | 1]`로 우산의 유무까지 포함한 3차원 방문 배열로 관리 -> 시간 초과 및 문제 해결 불가
  3. 2에서 발생할 수 있는 잠재적인 문제는 둘다 우산이 있는 상태여도 우산의 내구도, 현재 체력 등이 달라질 수 있음. 즉, 우산 유무만으로 처리하게 되면 더 좋은 상태로 도착하는 케이스를 무시하게 됨
     a. 따라서, 앞으로 얼마나 더 버틸 수 있는지에 대한 값(h + u)을 바탕으로 방문 처리를 하는 것이 좋음. -> 현재 체력 + 현재 우산 내구도. visited 배열 값보다 h + u 이 더 크다면 지금 상태가 더 좋으니 다시 탐색할 가치가 있음. 반대면 탐색 가치가 없으므로 생략

### 동전 게임 (9079)

```python
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    board = []
    for _ in range(3):
        board.append(list(input().rstrip().split()))


def reverse(board, dir, index):
    if dir == 'x':
        for i in range(3):
            board[index][i] = 'T' if board[index][i] == 'H' else 'H'

    elif dir == 'y':
        for i in range(3):
            board[i][index] = 'T' if board[i][index] == 'H' else 'H'

def complete(board):
    tail_count = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'T':
                tail_count += 1

    return tail_count == 0 or tail_count == 9


def game(board, count = 0):
    if (complete(board)):
        print(count)
        exit()

    for dir in ['y', 'x']:
        for i in range(3):
            reverse(board, dir, i)
            game(board, count + 1)
            reverse(board, dir, i)

game(board)

```

- 초기 코드는 위와 같은 틀로 만들었는데, 위 코드 기준으로 핵심 문제 2가지는 아래와 같음.

  1. 같은 상태를 무한히 다시 방문할 수 있음.
  2. 애초에 도달 불가능한 상태를 판별하지 못함.

- New Idea
  1. 각 연산은 안 하거나 1번 하거나만 의미가 있음 -> 2번은 원상복구여서 안해도 됨.

- 추가로 막힌 부분

1. BFS 수행 시, 객체 복사 -> 현재는 연산 수가 적어서 괜찮았는데 많은 경우에 어떻게 대응할지는 좀 더 학습이 필요해보임. 
2. 1와 비슷한 이유로 비트 마스킹..을 적용하면 풀이 자체도 쉬워지고 불필요한 객체 복사 안해도 될듯