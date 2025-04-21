def solution(s):
    answer = []
    arr = s.split(' ')
    for c in arr:
        if c:
            answer.append(c.lower().capitalize())
        else:
            answer.append("")
    return " ".join(answer)