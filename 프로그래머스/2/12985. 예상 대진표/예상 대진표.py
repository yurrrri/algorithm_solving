import math

def solution(n,a,b):
    for i in range(1, n+1):
        if (a%2 == 0 and b%2 != 0 and a-b == 1) or (a%2 != 0 and b%2 == 0 and b-a == 1):
            break
        a = math.ceil(a/2)
        b = math.ceil(b/2)
            
    return i