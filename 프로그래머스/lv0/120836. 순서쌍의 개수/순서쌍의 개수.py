def solution(n):
    return len(list(i for i in range(1, n+1) if n%i == 0))