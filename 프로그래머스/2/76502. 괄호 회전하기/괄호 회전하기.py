def isCorrectGwalho(s):
    stack = []
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        else:
            if len(stack) == 0:   # 닫는 괄호를 만나는 시점에서 스택이 비어있다면 이미 올바른 문자열이 아니므로 early return 처리한다.
                return False
            
            if (stack[-1] == "(" and c == ")") or (stack[-1] == "[" and c == "]") or (stack[-1] == "{" and c == "}"):
                stack.pop() 
                
    return len(stack) == 0   # 스택이 비어있음 -> 즉, 모든 괄호가 상쇄되므로 return true

def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        s += s.pop(0)
        if isCorrectGwalho(s):
            answer += 1
    return answer