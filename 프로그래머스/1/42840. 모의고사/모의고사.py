def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    one_score, two_score, three_score = (0, 0, 0)
    for i, answer in enumerate(answers):
        j = i%len(one)
        k = i%len(two)
        l = i%len(three)
        
        if answer == one[j]:
            one_score += 1
            
        if answer == two[k]:
            two_score += 1
            
        if answer == three[l]:
            three_score += 1
            
    max_score = max(one_score, two_score, three_score)
    answer = [r[0] for r in [(1, one_score), (2, two_score), (3, three_score)] if r[1] == max_score]
            
    return answer