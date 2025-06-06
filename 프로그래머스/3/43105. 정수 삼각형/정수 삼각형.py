def solution(triangle):
    n = len(triangle[-1])
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = triangle[0][0]
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:     # 첫번째일 경우 첫번째꺼 그대로 내려옴
                arr[i][0] = triangle[i][0] + arr[i-1][0]
            elif j == i:    # 마지막일 경우는 마지막 그대로 내려옴
                arr[i][j] = triangle[i][j] + arr[i-1][i-1]
            else:
                arr[i][j] = triangle[i][j] + max(arr[i-1][j-1], arr[i-1][j])
                            
    return max(arr[-1])