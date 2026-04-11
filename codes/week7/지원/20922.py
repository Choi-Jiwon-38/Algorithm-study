import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
counter = dict()

i, j, answer = 0, 0, 1
counter[a[i]] = 1

while j < n - 1:
    j += 1
    if a[j] in counter:
        counter[a[j]] += 1
    else:
        counter[a[j]] = 1

    if counter[a[j]] > k: # 개수 제한을 넘은 경우
        while counter[a[j]] > k:
            counter[a[i]] -= 1
            i += 1

    answer = max(j - i + 1, answer)

print(answer)