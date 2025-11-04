from collections import Counter

def solution(participant, completion):
    counter = Counter(participant) - Counter(completion)
    # counter 집합을 차집합 연산했을 때, value가 0인 경우 해당 개체가 제거된다.
        
    return list(counter.keys())[-1]