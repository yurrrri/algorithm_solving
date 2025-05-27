def solution(schedules, timelogs, startday):
    answer = 0
    
    for i, schedule in enumerate(schedules):    # 각각의 출근 희망시각
        deadline = schedule + 10    # 출근 인정시각 (10분 더함)
        if int(str(deadline)[1:]) >= 60:   # 10분 더한 출근 인정시간이 앞의 시가 바뀌었을 떄 (예를들어 8시 55분에서 10분 더하면 9시 5분일 경우)
            deadline += 40                # 100을 더한다음 60을 빼는 작업이기때문에 기존 출근 인정시간에 40을 더하면 됨
        day = startday
        flag = False
        for timelog in timelogs[i]:
            if day % 7 == 6 or day % 7 == 0:    # 토욜이나 일욜일 경우 day를 더해주되 로직을 건너뜀
                day += 1
                continue
            day += 1
            if timelog > deadline:    # 하나라도 지각한게 있다면 그 직원은 탈락
                flag = True
                break
        
        if not flag:
            answer += 1
        
    return answer