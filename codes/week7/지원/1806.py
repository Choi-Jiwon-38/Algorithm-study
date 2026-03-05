import sys
input = sys.stdin.readline

n, s = map(int, input().split())
a = list(map(int, input().split()))
i, j, answer = 0, 0, None
curr_sum = a[i]

if sum(a) < s:
    print(0)
    exit()

while j < n - 1:
    while curr_sum < s and j < n - 1:
        j += 1
        curr_sum += a[j]
    
    if not answer:
        answer = j - i + 1
    else:
        answer = min(answer, j - i + 1)

    while curr_sum >= s:
        curr_sum -= a[i]
        i += 1

        if curr_sum >= s:
            answer = min(answer, j - i + 1)

print(answer)