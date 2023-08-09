def solution(s):
    splited = sorted(s[2:-2].split("},{"), key=lambda x:len(x))
    dic = {}
    
    for tup in splited:
        tup = list(map(int, tup.split(',')))
        for t in tup:
            if t not in dic:
                dic[t] = 1
                
    return list(dic)