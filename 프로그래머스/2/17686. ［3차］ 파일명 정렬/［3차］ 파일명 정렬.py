from functools import cmp_to_key

def compare(a, b):
    def split(file):
        head = ''
        number = ''
        i = 0
        length = len(file)

        # HEAD 추출: 숫자 이전까지
        while i < length and not file[i].isdigit():
            head += file[i]
            i += 1

        # NUMBER 추출: 숫자가 끝날 때까지 (제한 없음)
        while i < length and file[i].isdigit():
            number += file[i]
            i += 1

        return head, number

    a_head, a_num = split(a)
    b_head, b_num = split(b)

    # HEAD 비교 (대소문자 무시)
    if a_head.lower() < b_head.lower():
        return -1
    elif a_head.lower() > b_head.lower():
        return 1
    else:
        # NUMBER 비교 (숫자 비교)
        if int(a_num) < int(b_num):
            return -1
        elif int(a_num) > int(b_num):
            return 1
        else:
            return 0  # 같으면 원래 순서 유지

def solution(files):
    return sorted(files, key=cmp_to_key(compare))
