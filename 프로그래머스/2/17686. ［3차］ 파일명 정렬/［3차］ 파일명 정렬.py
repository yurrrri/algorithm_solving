from functools import cmp_to_key

def compare(a, b):
    axis = 0          # 1이면 뒤, 0이면 그대로, -1이면 앞으로 정렬하기 이므로, 해당 값을 반환하기 위한 축
    
    def extract_from_file(file):

        # 1) HEAD 분리 작업
        head_end_index = 1    # 최소한 1글자 이상이므로 초기값 1
        
        for i in range(len(file)):
            if file[i].isdigit():
                head_end_index = i
                break
                
        # 2) NUMBER 분리 작업
        
        number_end_index = len(file)    # 위 틀린 코드에서 수정한 부분

        for i in range(head_end_index, len(file)):
            if not file[i].isdigit():   # number가 시작하는 지점부터 끝까지의 범위에서 처음으로 숫자가 아닌 수가 나타나는 구간이 number임
                number_end_index = i
                break
                
        return file[:head_end_index], file[head_end_index:number_end_index]
    
    a_header, a_number = extract_from_file(a)
    b_header, b_number = extract_from_file(b)

    if a_header.lower() > b_header.lower():
        axis = 1
    elif a_header.lower() < b_header.lower():
        axis = -1
    else:
        if int(a_number) > int(b_number):
            axis = 1
        elif int(a_number) < int(b_number):
            axis = -1
        else:
            axis = 0

    return axis

def solution(files):
    return sorted(files, key=cmp_to_key(compare))
