from collections import Counter

def solution(clothes):
    arr = [i[1] for i in clothes]
    counter = Counter(arr)
    answer = 1
    
    for v in counter.values():
        answer *= (v+1)
    return answer-1