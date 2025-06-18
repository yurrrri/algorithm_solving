from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses_q = deque(progresses)
    speeds_q = deque(speeds)
    
    while progresses_q:
        while progresses_q[0] < 100:
            for i in range(len(progresses_q)):
                progresses_q[i] += speeds_q[i]
                
        _sum = 0
        while progresses_q and progresses_q[0] >= 100:
            _sum += 1
            progresses_q.popleft()
            speeds_q.popleft()
            
        answer.append(_sum)
        
    return answer