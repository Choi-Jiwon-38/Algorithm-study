import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
commands = list(map(int, input().split()))

max_num = -float('inf')
min_num = float('inf')


def backtrack(num: int, step = 0):
    global n, min_num, max_num
    
    if step == n - 1:
        max_num = max(num, max_num)
        min_num = min(num, min_num)
        return

    for i in range(4):
        if commands[i] == 0:
            continue
        
        commands[i] -= 1

        calculated_num = num

        if i == 0:
            calculated_num += a[step + 1]
        elif i == 1:
            calculated_num -= a[step + 1]
        elif i == 2:
            calculated_num *= a[step + 1]
        elif i == 3:
            if calculated_num < 0:
                calculated_num *= - 1
                calculated_num //= a[step + 1]
                calculated_num *= - 1
            else:
                calculated_num //= a[step + 1] 

        backtrack(calculated_num, step + 1)
        commands[i] += 1

backtrack(a[0])

print(max_num)
print(min_num)