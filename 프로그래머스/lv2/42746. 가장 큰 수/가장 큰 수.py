from functools import cmp_to_key

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    
    if t1 > t2:
        return 1
    elif t1 == t2:
        return 0
    else:
        return -1

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer