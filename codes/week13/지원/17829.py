import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int , input().split())))

def return_second(start_y, start_x):
    num_list = [
        arr[start_y][start_x],
        arr[start_y][start_x + 1],
        arr[start_y + 1][start_x],
        arr[start_y + 1][start_x + 1]
    ]

    num_list.sort()

    return num_list[-2]


while n >= 2:
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            arr[i // 2][j // 2] = return_second(i, j)

    n //= 2

print(arr[0][0])