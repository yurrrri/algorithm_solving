def solution(land):
    answer = 0
    n = len(land)
    
    for i in range(1, n):
        for j in range(4):
            temp = 0
            for k in range(4):
                if j != k:
                    temp = max(land[i-1][k], temp)
            land[i][j] += temp

    return max(land[-1])