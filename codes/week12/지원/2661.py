import sys
input = sys.stdin.readline

num_strs = ['1', '2', '3']
n = int(input())

def check(str_num: str):
    l = len(str_num)
    
    for size in range(1, l // 2 + 1):
        if str_num[-size:] == str_num[-size * 2:-size]:
            return False

    return True

def make(prev_num_str: str):
    global answer
    if len(prev_num_str) == n:
        print(prev_num_str)
        exit()
    

    for num_str in num_strs:
        if check(prev_num_str + num_str):
            make(prev_num_str + num_str)
    

for num_str in num_strs:
    make(num_str)
