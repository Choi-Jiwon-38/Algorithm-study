import sys
import heapq
input = sys.stdin.readline

max_heapq = []
min_heapq = []

problem_list = {}

def update_heaps(problem, level):
    heapq.heappush(max_heapq, (-level, -problem))
    heapq.heappush(min_heapq, (level, problem))

    problem_list[problem] = level


n = int(input())

for _ in range(n):
    p, l = map(int, input().split())
    update_heaps(p, l)

m = int(input())

for _ in range(m):
    inputList = list(input().rstrip().split())

    if inputList[0] == 'add':
        p, l = int(inputList[1]), int(inputList[2])
        update_heaps(p, l)

    elif inputList[0] == 'recommend':
        if inputList[1] == '1':
            while True:
                level, max_num = max_heapq[0]
                level *= -1
                max_num *= -1

                if problem_list[max_num] != level:
                    heapq.heappop(max_heapq)
                    continue
                else:
                    print(max_num)
                    break

        else: # inputList[1] == '-1:
            while True:
                level, min_num = min_heapq[0]

                if problem_list[min_num] != level:
                    heapq.heappop(min_heapq)
                    continue
                else:
                    print(min_num)
                    break
    
    elif inputList[0] == 'solved':
        problem_list[int(inputList[1])] = -1