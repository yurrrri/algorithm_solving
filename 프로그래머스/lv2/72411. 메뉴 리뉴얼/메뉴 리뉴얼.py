from collections import Counter
from itertools import combinations

# def solution(orders, course):
#     arr = []
#     for c in course:
#         for order in orders:
#             arr += list(combinations(sorted(order), c))
            
#     counter = dict(Counter(arr))
    
#     count = [0] * len(course)
    
#     for c in range(len(course)):
#         for k, v in counter.items():
#             if len(k) == course[c] and count[c] < v:
#                 count[c] = v
                
#     answer = []
#     for c in range(len(course)):
#         for k, v in counter.items():
#             if v >= 2 and count[c] == v and course[c] == len(k):
#                 answer.append(k)
                
#     return sorted(answer)

# 다른 풀이
def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common() # course_size의 조합 중 가장 많이 주문된 순서대로 정렬된 배열
        result += [k for k, v in most_ordered if v>=2 and v == most_ordered[0][1] ]

    return [''.join(v) for v in sorted(result) ]