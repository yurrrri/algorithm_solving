from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    sorted_counter = sorted(counter.items(), key=lambda x:-x[1])
    answer = 0
    
    for key, value in sorted_counter:
        if k <= 0:
            break
        k -= value
        answer += 1
    return answer