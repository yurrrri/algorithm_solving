from functools import cmp_to_key

def compare(a, b):
    
    axis = 0
    
    def extract_from_file(file):

        head, number, tail = ("", "", "")
        number_start_idx = 0

        for idx, f in enumerate(file):
            if number_start_idx == 0 and f.isdigit():
                head = file[:idx]
                number_start_idx = idx
            elif number_start_idx != 0 and not f.isdigit():
                number = file[number_start_idx:idx]
                tail = file[idx:]
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
    else:
        if int(a_number) < int(b_number):
            axis = -1
        elif int(a_number) > int(b_number):
            axis = 1
        else:
            axis = 0
        
    return axis

def solution(files):
    return sorted(files, key=cmp_to_key(compare))