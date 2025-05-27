def solution(schedules, timelogs, startday):
    answer = 0
    for i, schedule in enumerate(schedules):    # 각각의 출근 희망시각
        deadline = schedule + 10    # 출근 인정시각 (10분 더함)
        if int(str(deadline)[1:]) >= 60:
            deadline += 40
        day = startday
        flag = False
        for timelog in timelogs[i]:
            if day % 7 == 6 or day % 7 == 0:
                day += 1
                continue
            day += 1
            if timelog > deadline:
                flag = True
                break
        
        if not flag:
            answer += 1
        
    return answer