def solution(dartResult):
    answer = 0
    stack = []
    dartResult = dartResult.replace('10', 'k')
    dartResult = ['10' if r == 'k' else r for r in dartResult]
        
    for dart in dartResult:
        if dart == "S":
            continue
        elif dart == "D":
            stack[-1] = stack[-1] ** 2
        elif dart == "T":
            stack[-1] = stack[-1] ** 3
        elif dart == "*":
            stack[-2:] = [r * 2 for r in stack[-2:]]
        elif dart == "#":
            stack[-1] *= (-1)
        else:
            stack.append(int(dart))
        
    return sum(stack)