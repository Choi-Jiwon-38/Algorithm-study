import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())

    high_priority_queue = []    # "D 1"이 입력되어 최댓값 삭제가 필요할 때 사용
    low_priority_queue = []     # "D -1"이 입력되어 최솟값 삭제가 필요할 때 사용
    num_dict = {}
    len_queue = 0

    for __ in range(k):
        cmd, num_str = input().rstrip().split()
        num = int(num_str)      # 형 변환 필요 주의

        if cmd == 'I':
            heapq.heappush(low_priority_queue, num)
            heapq.heappush(high_priority_queue, -num)
            len_queue += 1      # len_queue는 공통으로 관리

            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1

        elif cmd == 'D':
            if len_queue == 0:  # 큐가 비었는데 적용할 연산이 'D'라면
                continue        # 연산을 무시

            len_queue -= 1      # len_queue는 공통으로 관리

            if num == 1:
                while True:
                    max_num = -heapq.heappop(high_priority_queue)
                    if num_dict[max_num] == 0:
                        continue
                    else:
                        num_dict[max_num] -= 1
                        break
                
            elif num == -1:
                while True:
                    min_num = heapq.heappop(low_priority_queue)
                    if num_dict[min_num] == 0:
                        continue
                    else:
                        num_dict[min_num] -= 1
                        break

    if len_queue == 0:
        print("EMPTY")

    else:
        max_value = -float('inf')
        min_value = float('inf')

        for num in num_dict.keys():
            if num_dict[num] == 0:
                continue
            
            if num > max_value:
                max_value = num
            
            if num < min_value:
                min_value = num

        print(max_value, min_value)