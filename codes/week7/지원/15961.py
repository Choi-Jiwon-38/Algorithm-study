import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
bobs = []
dict = {}
answer = 0

for _ in range(n):
    bobs.append(int(input()))

# circular queue
for i in range(k): 
    bobs.append(bobs[i])

# coupon
dict[c] = 1


# init
for i in range(k):
    if bobs[i] in dict:
        dict[bobs[i]] += 1
    else:
        dict[bobs[i]] = 1

def remove_bob(bob):
    if dict[bob] == 1:
        dict.pop(bob)
    else:
        dict[bob] -= 1

def add_bob(bob):
    if bob in dict:
        dict[bob] += 1
    else:
        dict[bob] = 1

def update_answer():
    global answer
    answer = max(answer, len(dict.keys()))

# index
i, j = 0, k - 1

while j < n + k - 1:
    remove_bob(bobs[i])
    i += 1
    j += 1
    add_bob(bobs[j])
    update_answer()

print(answer)    