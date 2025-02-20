# 여기서 중복되는 코드는 하나의 변수로 만들면 좋을듯
def solution(a, b, c):
    if len(set([a, b, c])) == 3:
        return a+b+c
    elif len(set([a, b, c])) == 2:
        return (a+b+c) * (a**2 + b**2 + c**2)
    else:
        return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)