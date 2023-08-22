from collections import deque

def solution(priorities, location):
    priority = [(idx, e) for idx, e in enumerate(priorities)]
    q = deque(priority)
    answer = 0
    
    while True:
        prior = q.popleft() # 1. 프로세스 꺼내기
        if not q:
            answer += 1
            break
        
        maxValue = max(q, key=lambda x:x[1])[1] # 우선순위 최대값
        if prior[1] < maxValue: # 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스 존재
            q.append(prior)
        else:
            answer += 1
            if prior[0] == location:
                break
                
    return answer