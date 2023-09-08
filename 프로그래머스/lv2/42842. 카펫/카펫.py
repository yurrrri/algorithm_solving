def solution(brown, yellow):
    _sum = brown + yellow
    for i in range(1, brown+1):
        for j in range(1, brown+1):
            if i*j == _sum and (i-2)*(j-2) == yellow:
                return [j, i]
            