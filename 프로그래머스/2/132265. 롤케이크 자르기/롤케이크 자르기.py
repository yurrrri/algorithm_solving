from collections import Counter

def solution(topping):
    answer = 0

    old = set()
    young = Counter(topping)
    
    for t in topping:
        old.add(t)
        young[t] -= 1
        
        if young[t] == 0:
            del young[t]
            
        if len(old) == len(young):
            answer += 1
    
    return answer