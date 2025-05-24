def solution(survey, choices):
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    jipyos = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    for i, s in enumerate(survey):
        if choices[i] < 4:
            dic[s[0]] += 4 - choices[i]
        elif choices[i] > 4:
            dic[s[1]] += choices[i] - 4
        
    answer = ''
    for a, b in jipyos:
        if dic[a] > dic[b]:
            answer += a
        elif dic[a] < dic[b]:
            answer += b
        else:
            answer += a
    
    return answer