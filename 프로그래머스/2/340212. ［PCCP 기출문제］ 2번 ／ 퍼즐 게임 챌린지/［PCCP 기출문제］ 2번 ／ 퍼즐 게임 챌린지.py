def solution(diffs, times, limit):
    start = 1
    end = max(diffs)
    answer = 0
    
    def calculate(level):   # level 별로 문제들을 푸는데 드는 총 소요 시간을 계산하는 함수
        sum_time = 0
        
        for i, (diff, time) in enumerate(zip(diffs, times)):
            if diff <= level:
                sum_time += time
            else:
                sum_time += (diff - level) * (times[i-1] + time) + time
                
        return sum_time
    
    while start <= end:
        mid = (start + end) // 2
        
        if calculate(mid) <= limit:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer