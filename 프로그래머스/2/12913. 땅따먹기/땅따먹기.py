def solution(land):
    answer = 0
    n = len(land)
    
    for i in range(1, n):
        for j in range(4):
            temp = max(land[i-1][:j] + land[i-1][j+1:])
            land[i][j] += temp

    return max(land[-1])