def ispair(string):
    stack = []
    
    for s in string:
        if s in ["[", "(", "{"]:
            stack.append(s)
        else:
            if not stack:
                return False
            if stack[-1] == "[" and s == "]" or stack[-1] == "(" and s == ")" or stack[-1] == "{" and s == "}":
                stack.pop()
            
    return len(stack) == 0
    

def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        s.insert(0, s.pop())
        if ispair(s):
            answer += 1
    
    return answer