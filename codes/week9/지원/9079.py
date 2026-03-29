import sys
from collections import deque
input = sys.stdin.readline

t = int(input())    

def reverse(board, num):
    if 0 <= num <= 2:
        index = num
        for i in range(3):
            board[index][i] = 'T' if board[index][i] == 'H' else 'H'

    elif 3 <= num <= 5:
        index = num - 3
        for i in range(3):
            board[i][index] = 'T' if board[i][index] == 'H' else 'H'

    elif num == 6:
        for i in range(3):
            board[i][i] = 'T' if board[i][i] == 'H' else 'H'

    elif num == 7:
        for i in range(3):
            board[i][2 - i] = 'T' if board[i][2 - i] == 'H' else 'H'

def complete(board):
    tail_count = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'T':
                tail_count += 1
    
    return tail_count == 0 or tail_count == 9

def game(board):
    q = deque([([False for _ in range(8)], board)])

    while q:
        flag, board = q.popleft()

        for i in range(8):
            if flag[i]:
                continue
            else:
                flag[i] = True
                reverse(board, i)

                if complete(board):
                    return flag.count(True)

                q.append((flag[:], [row[:] for row in board]))
                flag[i] = False
                reverse(board, i)
    
    return -1


for _ in range(t):
    board = []
    for _ in range(3):
        board.append(list(input().rstrip().split()))
    
    if complete(board):
        print(0)
    else:
        result = game(board)
        print(result)
