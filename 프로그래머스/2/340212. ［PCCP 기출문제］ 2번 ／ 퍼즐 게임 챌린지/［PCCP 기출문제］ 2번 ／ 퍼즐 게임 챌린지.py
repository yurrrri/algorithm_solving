def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    
    def calculate(level):
        sum_time = 0
        
        for i, (diff, time) in enumerate(zip(diffs, times)):
            if diff <= level:
                sum_time += time
            else:
                sum_time += (diff - level) * (times[i-1] + time) + time
                
        if sum_time <= limit:
            return True
        else:
            return False
    
    while start <= end:
        mid = (start + end) // 2
        
        if calculate(mid):
            end = mid - 1
        else:
            start = mid + 1

    return start