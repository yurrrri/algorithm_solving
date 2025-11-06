from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dic = {}
    
    for p, n in zip(want, number):
        want_dic[p] = n
        
    for i in range(len(discount)-9):
        counter = Counter(discount[i:i+10])
        if counter == want_dic:
            answer += 1
    
    return answer