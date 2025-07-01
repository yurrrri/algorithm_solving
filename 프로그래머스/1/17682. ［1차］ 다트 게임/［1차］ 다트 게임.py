def solution(dartResult):
    answer = 0
    stack = []
        
    for dart in dartResult:
        if dart == "S":
            continue
        elif dart == "D":
            stack[-1] = stack[-1] ** 2
        elif dart == "T":
            stack[-1] = stack[-1] ** 3
        elif dart == "*":
            stack[-1] *= 2
            if len(stack) >= 2:
                stack[-2] *= 2
        elif dart == "#":
            stack[-1] *= (-1)
        else:
            if stack and stack[-1] == 1 and dart == "0":
                stack.pop()
                stack.append(10)
            else:
                stack.append(int(dart))
        
    return sum(stack)