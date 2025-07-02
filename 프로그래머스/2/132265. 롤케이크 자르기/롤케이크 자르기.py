from collections import Counter

def solution(topping):
    answer = 0
    s1 = set()
    s2 = Counter(topping)
    
    for t in topping:
        s1.add(t)
        s2[t] -= 1
        if s2[t] == 0:
            del s2[t]
            
        if len(s1) == len(s2):
            answer += 1
    
    return answer