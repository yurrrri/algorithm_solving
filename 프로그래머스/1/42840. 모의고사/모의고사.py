def solution(answers):
    answer = []
    scores = [0] * 3
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            scores[0] += 1
        if second[i%8] == answers[i]:
            scores[1] += 1
        if third[i%10] == answers[i]:
            scores[2] += 1
            
    maxscore = max(scores)
    for i, e in enumerate(scores):
        if e == maxscore:
            answer.append(i+1)
    
    return answer