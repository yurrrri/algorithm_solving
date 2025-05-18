def solution(brown, yellow):
    _sum = brown + yellow
    for i in range(3, brown+1):   # 세로
        for j in range(3, brown+1):    # 가로
            if i*j == _sum and (i-2)*(j-2) == yellow:
                return [j, i]