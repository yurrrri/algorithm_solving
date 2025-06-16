def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0] * 3
    for i, answer in enumerate(answers):
        j = i%len(one)
        k = i%len(two)
        l = i%len(three)
        
        if answer == one[j]:
            scores[0] += 1
            
        if answer == two[k]:
            scores[1] += 1
            
        if answer == three[l]:
            scores[2] += 1
            
    max_score = max(scores)
    answer = [i+1 for i, score in enumerate(scores) if score == max_score]
            
    return answer