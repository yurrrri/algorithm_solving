from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    speed_queue = deque(speeds)
    
    answer = []
    count = 0
    
    while len(queue) > 0:  # 모든 작업이 끝날떄까지 반복
        while queue[0] < 100:   # 앞 작업 진척률이 100 되기 전까지 모든 작업상황들 진척상황 업데이트
            for i in range(len(speed_queue)):
                queue[i] += speed_queue[i]
                
        while len(queue) > 0 and queue[0] >= 100:  # 앞에 있는 작업이 100 넘는것들은 모두 배포
            queue.popleft()
            speed_queue.popleft()
            count += 1
            
        answer.append(count)
        count = 0
        
    return answer