from collections import Counter

def solution(participant, completion):
    counter = Counter(participant) - Counter(completion)
        
    return list(counter.keys())[-1]