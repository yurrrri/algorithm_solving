from collections import Counter

def solution(want, number, discount):
    answer = 0
    want_dic = {}
    for w, n in zip(want, number):
        want_dic[w] = n
        
    for i in range(len(discount)):
        counter = Counter(discount[i:i+10])
        if want_dic == counter:
            answer += 1
        
    return answer