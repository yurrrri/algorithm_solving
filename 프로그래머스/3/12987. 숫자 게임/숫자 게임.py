def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    
    idx_A, idx_B = 0, 0
    while idx_A < len(A) and idx_B < len(B):
        if A[idx_A] < B[idx_B]:
            idx_A += 1
            idx_B += 1
            answer += 1
        else:
            idx_B += 1
    
    return answer