from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    orders = [sorted(i) for i in orders]
    menus = []
    combi_max = {}
    for c in course:
        combi_max[c] = 0
    
    for order in orders:
        for number in course:
            combi = combinations(order, number)
            for c in combi:
                menus.append("".join(c))
                
    counter = Counter(menus)
    for menu, count in counter.items():
        for c in course:
            if len(menu) == c:
                combi_max[c] = max(combi_max[c], count)
                
    for menu, count in counter.items():
        for c in course:
            if len(menu) == c and count >= 2 and count == combi_max[c]:
                answer.append(menu)
    
    answer.sort()
    
    return answer