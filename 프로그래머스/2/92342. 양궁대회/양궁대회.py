from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):             # info: 어피치가 맞힌 화살 리스트, 차례대로 10-9-8-7-6... 등
    answer = [0] * 11
    maxdiff, maxcombi = 0, {}
    
    def calculate_score(combi):
        score1, score2 = 0, 0
        
        for i in range(1, 11):
            if not info[10-i] and not combi[i]:
                continue
                
            if info[10-i] < combi[i]:
                score2 += i
            else:
                score1 += i
                
        return score1, score2
    
    for combi in combinations_with_replacement(range(11), n):
        counter = Counter(combi)
        apeach, ryan = calculate_score(counter)
        
        diff = ryan - apeach
        if diff > maxdiff:
            maxdiff = diff
            maxcombi = counter
            
    if maxdiff > 0:
        for i in range(11):
            answer[10-i] = maxcombi[i]
            
        return answer
    else:
        return [-1]