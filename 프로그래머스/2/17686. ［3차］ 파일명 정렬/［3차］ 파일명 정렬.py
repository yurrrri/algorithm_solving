from functools import cmp_to_key

def compare(a, b):
    def split(file):
        head_end_index = 0
        number_end_index = len(file)

        for i in range(len(file)):
            if file[i].isdigit():
                head_end_index = i
                break

        for i in range(head_end_index, len(file)):
            if not file[i].isdigit():
                number_end_index = i
                break

        header = file[:head_end_index]
        number = file[head_end_index:number_end_index]
        return header, number

    a_header, a_number = split(a)
    b_header, b_number = split(b)

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