from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    speed_queue = deque(speeds)
    
    answer = []
    count = 0
    
    while len(queue) > 0:
        while queue[0] < 100:
            for i in range(len(speed_queue)):
                queue[i] += speed_queue[i]
                
        while len(queue) > 0 and queue[0] >= 100:
            queue.popleft()
            speed_queue.popleft()
            count += 1
            
        answer.append(count)
        count = 0
        
    return answer