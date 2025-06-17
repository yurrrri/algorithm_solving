def solution(prices):
    answer = [0] * len(prices)
    stack = [0]
    
    for i in range(1, len(prices)):
        if prices[stack[-1]] > prices[i]:
            while stack and prices[stack[-1]] > prices[i]:
                j = stack.pop()
                answer[j] = i - j
        stack.append(i)
                
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
    return answer