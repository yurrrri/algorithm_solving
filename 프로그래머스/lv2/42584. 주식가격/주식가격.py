def solution(prices):
    answer = [0] * len(prices)
    stack = []   # 인덱스를 쌓아둘 스택
    
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            poped = stack.pop()
            answer[poped] = i - poped
            
        stack.append(i)   # 1. 차례대로 인덱스를 추가함
        
    for i in stack:
        answer[i] = len(prices) - 1 - i
        
    return answer