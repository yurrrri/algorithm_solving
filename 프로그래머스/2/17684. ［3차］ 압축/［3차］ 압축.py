from collections import deque

def solution(msg):
    answer = []
    dic = {}
    for i in range(1, 27):          # 색인 사전
        dic[chr(ord('A') + i - 1)] = i
        
    queue = deque(msg)
    while queue:
        temp = queue.popleft()
        while queue and temp + queue[0] in dic:
            temp += queue.popleft()
        answer.append(dic[temp])
        if queue:
            dic[temp+queue[0]] = len(dic) + 1
            
    return answer