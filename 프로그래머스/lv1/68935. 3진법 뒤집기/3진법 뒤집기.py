def radixChange(n, radix):
    arr = []
    while n:
        n, remain = divmod(n, radix)
        arr.append(str(remain))
        
    return ''.join(arr[::-1])

def solution(n):
    answer = 0
    arr = radixChange(n, 3)
    
    print(arr)
    
    return int(arr[::-1], 3)
    # return 0