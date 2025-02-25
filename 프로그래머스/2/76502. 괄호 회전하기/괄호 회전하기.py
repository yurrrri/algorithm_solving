def isCorrectGwalho(s):
    stack = []
    for c in s:
        if c in ["(", "[", "{"]:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            
            if (stack[-1] == "(" and c == ")") or (stack[-1] == "[" and c == "]") or (stack[-1] == "{" and c == "}"):
                stack.pop() 
                
    return len(stack) == 0

def solution(s):
    answer = 0
    temp = list(s)
    for _ in range(len(s)):
        temp += temp.pop(0)
        if isCorrectGwalho(temp):
            answer += 1
    return answer