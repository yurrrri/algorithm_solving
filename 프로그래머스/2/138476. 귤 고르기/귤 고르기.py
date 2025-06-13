from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    sorted_counter = sorted(counter.values(), reverse=True)
    answer = 0
    
    for value in sorted_counter:
        if k <= 0:
            break
        k -= value
        answer += 1
    return answer