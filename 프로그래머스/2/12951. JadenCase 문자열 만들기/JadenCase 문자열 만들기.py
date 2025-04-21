def solution(s):
    answer = []
    arr = s.split(' ')
    for c in arr:
        if c:
            answer.append(c.lower().capitalize())
        else:
            answer.append('')   # 공백 문자의 갯수대로 리스트에 공백 문자 포함
    return " ".join(answer)