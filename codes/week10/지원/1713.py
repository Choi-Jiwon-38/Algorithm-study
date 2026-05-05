import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

nums = list(map(int, input().split()))
votes = {}
pictures = []

def hanging_picture(num):
    min_vote = float('inf')
    min_vote_student = 0

    for i in range(len(pictures)):
        # 이미 타겟 num이 사진틀에 걸려있는 경우, 아무 행동 X
        if pictures[i] == num:
            votes[num] += 1
            return
        
        # 사진틀 중 가장 추천이 적은 추천 횟수 기억
        if votes[pictures[i]] < min_vote:
            min_vote = votes[pictures[i]]
            min_vote_student = pictures[i]

    # 사진틀에 사진을 걸 수 있는 경우    
    if len(pictures) < n:
        pictures.append(num)
        votes[num] = 1
        return

    # 사진틀이 꽉 찬 경우에는 가장 투표수 적은 거 지우고 append
    pictures.remove(min_vote_student)
    # 사진틀에서 게시된 사진이 삭제되는 경우, 추천 횟수 0으로 초기화
    votes[min_vote_student] = 0
    pictures.append(num)
    votes[num] = 1


for num in nums:
    hanging_picture(num)


pictures.sort()
print(*pictures)