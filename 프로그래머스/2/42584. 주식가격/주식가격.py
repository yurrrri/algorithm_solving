def solution(prices):
    n = len(prices)
    answer = [0] * n      # 길이를 저장할 배열
    stack = []        # 뒤에서부터 비교하므로 스택 사용
    stack.append(0)   # 처음은 비교대상이 없으므로 먼저 0 푸시해줌
    
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]: # 그 전에 있는 애랑 비교해서 더 크면 길이 확정지움
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        answer[j] = n-1-j
        
    return answer