from functools import cmp_to_key

def compare(a, b):
    
    axis = 0    # 기준 1, 2에서 모두 비교할 수 없을 경우 원래 입력에 주어진 순서를 유지하므로, 초기값을 0으로 세팅한다.
    
    def extract_from_file(file):
        number_start_idx = 0
        tail_start_idx = len(file)
        
        for i, s in enumerate(file):
            if s.isdigit():
                number_start_idx = i
                break
                
        for j in range(number_start_idx, len(file)):
            if not file[j].isdigit():
                tail_start_idx = j
                break
                
        return file[:number_start_idx], file[number_start_idx:tail_start_idx], file[tail_start_idx:]
        
    a_head, a_number, a_tail = extract_from_file(a)
    b_head, b_number, b_tail = extract_from_file(b)
    
    if a_head.lower() < b_head.lower():    # 문자열 비교시 대소문자 구분을하지 않으므로 둘다 lower 혹은 upper 처리하여 비교한다.
        # cmp_to_key의 함수에서 음수는 a가 b보다 앞에 오는 것이고, 양수는 a가 b보다 뒤에 오는것이다.
        axis = -1
    elif a_head.lower() > b_head.lower():
        axis = 1
    else:     # HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다.
        if int(a_number) < int(b_number):
            axis = -1
        elif int(a_number) > int(b_number):
            axis = 1
        else:   # HEAD와 NUMBER도 같을 경우, 원래 입력에 주어진 순서를 유지한다. (0 반환)
            axis = 0
            
    return axis

def solution(files):
    return sorted(files, key=cmp_to_key(compare))