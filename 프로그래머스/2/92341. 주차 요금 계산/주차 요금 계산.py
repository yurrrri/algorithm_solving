from collections import defaultdict
import math

def solution(fees, records):
    # fees: 차례대로 기본 시간, 기본 요금, 단위 시간, 단위 요금
    basic_time, basic_fee, unit_time, unit_fee = fees
    # answer: 차량번호가 작은 자동차부터 주차요금 차례대로 담아서 return
    record_dic = {}
    time_dic = defaultdict(int)
    
    def calculate_time(in_time, out_time):
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
        
    list_time_dic = sorted(time_dic.items(), key=lambda x:x[0])   # 차량 번호가 작은 순서부터 계산하기 위해 먼저 key 기준으로 정렬
    answer = []
    
    for _, time in list_time_dic:
        if time <= basic_time:
            answer.append(basic_fee)
        else:
            fee = basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee
            answer.append(fee)
    return answer