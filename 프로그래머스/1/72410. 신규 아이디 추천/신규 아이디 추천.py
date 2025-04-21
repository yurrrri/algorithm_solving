def solution(new_id):
    # 1단계
    answer = new_id.lower()
    # 2단계
    temp = ""
    for c in answer:
        if c.islower() or c.isdigit() or c in ["-", "_", "."]:
            temp += c
    answer = temp
    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")
    # 4단계
    answer = answer.strip(".")
    # 5단계
    if len(answer) == 0: # == not answer로 치환 가능
        answer = "a"
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip(".")
    # 7단계
    if len(answer) <= 2:
        last = answer[-1]
        while len(answer) < 3:
            answer += last
    return answer