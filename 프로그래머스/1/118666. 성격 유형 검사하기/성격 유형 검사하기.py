from collections import defaultdict

def solution(survey, choices):
    dic = defaultdict(int)
    jipyos = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for i, s in enumerate(survey):
        if choices[i] < 4:
            dic[s[0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[s[1]] += choices[i] - 4
        
    answer = ''
    for a, b in jipyos:
        if dic[a] >= dic[b]:
            answer += a
        else:
            answer += b
    
    return answer