from functools import cmp_to_key

def compare(a, b):
    
    axis = 0    # 기준 1, 2에서 모두 비교할 수 없을 경우 원래 입력에 주어진 순서를 유지하므로, 초기값을 0으로 세팅한다.
    
    def extract_from_file(file):

        head, number, tail = ("", "", "")
        number_start_idx = 0

        for idx, f in enumerate(file):
            if f.isdigit():
                head = file[:idx]
                number_start_idx = idx
                break
                
        for i in range(number_start_idx, len(file)):
            if not file[i].isdigit():
                number = file[number_start_idx:i]
                tail = file[i:]
                break
                
        if len(number) == 0:
            number = file[number_start_idx:]

        return head, number, tail
    
    a_head, a_number, a_tail = extract_from_file(a)
    b_head, b_number, b_tail = extract_from_file(b)
    
    if a_head.lower() < b_head.lower():
        axis = -1
    elif a_head.lower() > b_head.lower():
        axis = 1
    else:     # HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다.
        if int(a_number) < int(b_number):
            axis = -1
        elif int(a_number) > int(b_number):
            axis = 1
        else:
            axis = 0
        
    return axis

def solution(files):
    return sorted(files, key=cmp_to_key(compare))