import sys
from collections import deque
input = sys.stdin.readline

N, H, D = map(int, input().split())
board = []
visited = []

start_pos = None

for i in range(N):
    row = list(input().rstrip())

    for j in range(N):
        if row[j] == 'S': # 시작 위치만 확인하고 break
            start_pos = (i, j)
            break
    
    visited.append([0 for _ in range(N)])
    board.append(row)

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(q):
    while (q):
        # y: 현재 y 좌표
        # x: 현재 x 좌표
        # u: 현재 우산 내구도
        # c: 이동 횟수
        # h: 현재 체력
        y, x, u, c, h = q.popleft()


        # 상하좌우로 이동한다.
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            nu = u
            nc = c
            nh = h

            # 이동할 곳이 격자 안인 경우에만 이동
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] < nu + nh:
                nc += 1

                if board[ny][nx] == 'E': # 이동한 곳이 안전지대 -> 종료
                    print(nc)
                    exit()

                if board[ny][nx] == 'U': # 이동한 곳에 우산이 있다면 우산을 든다.
                    nu = D

                # 비 내리기
                if nu > 0:
                    nu -= 1
                else:
                    nh -= 1
                    
                if nh > 0 and visited[ny][nx] < nu + nh:
                    visited[ny][nx] = nu + nh
                    q.append((ny, nx, nu, nc, nh))
        
    print(-1)


sy, sx = start_pos

q = deque([(sy, sx, 0, 0, H)])
visited[sy][sx] = H
bfs(q)