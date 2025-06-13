def solution(d, budget):
    answer = 0
    d = sorted(d)
    budget = budget
    
    for money in d:
        if budget - money >= 0:
            budget -= money
            answer += 1
        else:
            break
    return answer