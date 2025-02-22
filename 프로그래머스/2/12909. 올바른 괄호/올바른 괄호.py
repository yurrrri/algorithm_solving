def solution(s):
    temp = []
    for c in s:
        if c == "(":
            temp.append("(")
        else:
            if len(temp) == 0:
                return False
            temp.pop()
    return len(temp) == 0