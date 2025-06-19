from collections import Counter

def solution(participant, completion):
    answer = ''
    counter = Counter(participant)
    
    for player in completion:
        counter[player] -= 1
        if counter[player] == 0:
            del counter[player]
        
    return list(counter.keys())[-1]