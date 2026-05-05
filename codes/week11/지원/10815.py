import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))
answer = []

def binary_search(target: int):
    s = 0
    e = n - 1

    while s <= e:
        m = (s + e) // 2

        if cards[m] == target:
            return answer.append(1)

        if cards[m] < target:
            s = m + 1
            continue

        if cards[m] > target:
            e = m - 1
            continue
    
    return answer.append(0)


for num in nums:
    binary_search(num)

print(*answer)