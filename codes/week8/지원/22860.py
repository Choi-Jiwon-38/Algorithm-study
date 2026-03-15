import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n, m = map(int, input().split())

children = {'main': []}
folders = {'main': []}

for i in range(n + m):
    p, f, c = input().rstrip().split()
    
    if c == '1': # 폴더
        if p in children:
            children[p].append(f)
        else:
            children[p] = [f]

        if not f in folders:
            folders[f] = []
    else: # 파일
        if p in folders:
            folders[p].append(f)
        else:
            folders[p] = [f]
    
def sync(curr):
    if not curr in children:
        return folders[curr]

    arr = []

    for child in children[curr]:
        arr += sync(child)
    
    folders[curr] += arr

    return folders[curr]

sync('main')

q = int(input())

for _ in range(q):
    paths = list(input().rstrip().split('/'))
    curr_folders = folders[paths[-1]]
    print(len(set(curr_folders)), len(curr_folders))