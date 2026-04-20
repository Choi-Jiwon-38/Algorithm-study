import sys
input = sys.stdin.readline

words = list(input().rstrip())
n = len(words)

visited = [False] * n


for i in range(n):
    target = ord('Z') + 1
    next_char_index = None

    for i in range(n):
        if visited[i]:
            target = ord('Z') + 1
        else:
            if ord(words[i]) < target:
                next_char_index = i
                target = ord(words[i])
    
    visited[next_char_index] = True
    answer = ''
  
    for i in range(n):
        if visited[i]:
            answer += words[i]

    print(answer)