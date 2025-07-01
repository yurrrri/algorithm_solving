def solution(dartResult):
    answer = 0
    stack = []
    dartResult = dartResult.replace('10', 'k')         # 10을 처리하기 위해 k로 바꾼다음, 아래에서 다시 10으로 바꿔줌
    # 이렇게 처리하기 까다로운 문자열이 포함되어있으면, replace를 활용하는 스킬을 떠올리자
    dartResult = ['10' if r == 'k' else r for r in dartResult]
        
    for dart in dartResult:
        if dart == "S":
            continue
        elif dart == "D":
            stack[-1] = stack[-1] ** 2
        elif dart == "T":
            stack[-1] = stack[-1] ** 3
        elif dart == "*":
            stack[-2:] = [r * 2 for r in stack[-2:]]      # 어차피 이전 점수가 없어도 리스트 슬라이싱은 인덱스 오류가 발생하지 않음
        elif dart == "#":
            stack[-1] *= (-1)
        else:
            stack.append(int(dart))
        
    return sum(stack)