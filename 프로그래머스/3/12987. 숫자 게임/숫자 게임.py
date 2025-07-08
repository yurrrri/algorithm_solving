def solution(A, B):
    A.sort()     # 차례대로 움직이며 B가 A보다 더 큰 원소를 찾아야하므로, 둘다 오름차순으로 정렬한다.
    B.sort()
    answer = 0
    
    idx_A, idx_B = 0, 0
    while idx_A < len(A) and idx_B < len(B):
        if A[idx_A] < B[idx_B]:
            idx_A += 1   # B가 더 큰 인덱스를 찾았으므로 그 다음 수를 비교하기 위해 idx_A, idx_B 둘다 + 1
            idx_B += 1
            answer += 1
        else:    # B가 더 큰 인덱스를 찾아다니기 위해 idx_B만 + 1
            idx_B += 1
    
    return answer