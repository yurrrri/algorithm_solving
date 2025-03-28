from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    combi = []
    
    for order in orders:
        order_to_list = sorted(list(order))
        for c in course:
            combi.extend(combinations(order_to_list, c))
            
    counter = Counter(combi)
    
    for c in course:
        max_num = 0
        for k, v in counter.items():
            if len(k) == c and v >= 2:
                max_num = max(max_num, v)
                
        for k, v in counter.items():
            if len(k) == c and v == max_num:
                answer.append("".join(k))
        
    return sorted(answer)