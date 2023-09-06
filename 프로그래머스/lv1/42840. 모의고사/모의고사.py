def solution(answers):
    one = [1, 2, 3, 4, 5] * 2000
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    count = [0] * 3
    
    for i in range(len(answers)):
        if answers[i] == one[i]:
            count[0] += 1
        if answers[i] == two[i]:
            count[1] += 1
        if answers[i] == three[i]:
            count[2] += 1
    _max = max(count)
    answer = []
    
    for i in range(3):
        if count[i] == _max:
            answer.append(i+1)
    
    return answer