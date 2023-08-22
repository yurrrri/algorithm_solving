def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
            
    if not stack:
        return True
    else:
        return False