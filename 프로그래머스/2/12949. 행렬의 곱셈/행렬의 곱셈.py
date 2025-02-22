def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])  # arr1의 행, 열 길이
    r2, c2 = len(arr2), len(arr2[0])  # arr2의 행, 열 길이
    answer = [[0] * c2 for _ in range(r1)] # 결과를 저장할 리스트 미리 초기화
    
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer