from functools import cmp_to_key

def compare(a, b):
    t1 = a + b
    t2 = b + a
    return (int(t1) > int(t2)) - (int(t1) < int(t2))
    # t1이 더 크면 1, t2이 더 크면 -1, 같으면 0 return

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = cmp_to_key(compare), reverse=True)
    return str(int(''.join(numbers)))
    