from functools import cmp_to_key

def compare(a, b):
    if int(a+b) > int(b+a):
        return -1
    elif int(a+b) == int(b+a):
        return 0
    else:
        return 1

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = int("".join(numbers))
    
    return str(answer)