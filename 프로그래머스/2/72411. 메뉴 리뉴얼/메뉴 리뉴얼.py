from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    orders = [sorted(i) for i in orders]   # 조합 내부의 알파벳도 정렬되어있어야하므로 먼저 정렬한다.
    
    for c in course:
        menus = []
        for order in orders:
            combi = combinations(order, c)
            for comb in combi:
                menus.append("".join(comb))
            
        counter = Counter(menus).most_common()
        
        for k, v in counter:
            if v >= 2 and v == counter[0][1]:
                answer.append(k)
                
    return sorted(answer)