def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        """
        2. 인덱스를 넣기 전에, stack의 마지막 인덱스가 현재보다 크다면 떨어졌다는 의미이므로 꺼내고 answer에 저장
        """
        while stack and prices[stack[-1]] > prices[i]: 
            past = stack.pop()
            answer[past] = i-past
        stack.append(i)  # 1. 차례대로 가격의 각 인덱스를 넣어줌
        
    for i in stack:
        answer[i] = len(prices) - 1 - i
    """
    3. 끝까지 상승세를 지속하다가 끝난 경우를 모두 계산함
    """
        
    return answer