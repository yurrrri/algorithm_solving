from collections import defaultdict
import math

def solution(fees, records):
    # fees: 차례대로 기본 시간, 기본 요금, 단위 시간, 단위 요금
    # answer: 차량번호가 작은 자동차부터 주차요금 차례대로 담아서 return
    record_dic = {}
    time_dic = defaultdict(int)
    
    def calculate_time(in_time, out_time):
        hour = 0
        minute = 0
        in_time = in_time.split(":")
        out_time = out_time.split(":")
        hour = int(out_time[0]) - int(in_time[0])
        minute = int(out_time[1]) - int(in_time[1])
        
        if minute < 0:
            minute += 60
            hour -= 1
            
        return hour * 60 + minute
    
    for record in records:
        time, number, command = record.split()
        if command == "IN":
            record_dic[number] = time
        else:   # 출차할 경우 시간 계산 후 time_dic에 추가
            time_dic[number] += calculate_time(record_dic[number], time)
            del record_dic[number]
            
    for (number, in_time) in record_dic.items():   # 출차되지 않은 차들은 23:59 out으로 침
        time_dic[number] += calculate_time(in_time, "23:59")
        
    list_time_dic = sorted(time_dic.items(), key=lambda x:x[0])
    print(list_time_dic)
    answer = []
    
    for _, time in list_time_dic:
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
            answer.append(fee)
    return answer