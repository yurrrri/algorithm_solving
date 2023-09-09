def radixChange(num, radix):
    nums = []
    while num > 0:
        mok, remain = divmod(num, radix)
        nums.append(remain)
        num = mok
        
    return ''.join(list(map(str, nums)))

def solution(n):
    answer = radixChange(n, 3)
    return int(answer, 3)