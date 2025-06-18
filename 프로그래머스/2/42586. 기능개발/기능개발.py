def solution(progresses, speeds):
    answer = []
    
    while progresses:
        while progresses[0] < 100:       # 무조건 앞에 있는 기능 먼저 배포할 수 있으므로, 앞에 있는 기능이 100을 넘을때까지 일함
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
                
        _sum = 0
        while progresses:
            if progresses[0] >= 100:       # 100이 넘는 작업들은 함께 배포
                _sum += 1
                progresses.pop(0)       # 배포
                speeds.pop(0)
            else:
                break
            
        answer.append(_sum)
        
    return answer