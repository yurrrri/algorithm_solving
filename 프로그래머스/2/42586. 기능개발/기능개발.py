def solution(progresses, speeds):
    answer = []
    
    while progresses:
        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]
                
        _sum = 0
        while progresses:
            if progresses[0] >= 100:
                _sum += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
            
        answer.append(_sum)
        
    return answer