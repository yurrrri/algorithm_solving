def solution(s):
    stack = []
    s = s.split()
    
    for c in s:
        if c != "Z":
            stack.append(int(c))
        else:
            stack.pop()
    return sum(stack)