import sys
input = sys.stdin.readline

count = 0 
dict = {}

for _ in range(1000000):
    ipt = input().rstrip()
    if (ipt == ''): break

    if ipt in dict:
        dict[ipt] += 1
    else:
        dict[ipt] = 1

    count += 1
    

keys = sorted(dict.keys())

for key in keys:
    print(f"{key} {(dict[key] / count * 100):.4f}")