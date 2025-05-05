def solution(s):
    s = s.replace("{{", "").replace("}}", "")
    s = s.split("},{")
    s = [a.split(',') for a in s]
    s = sorted(s, key=lambda x:len(x))
    answer = []
    
    for arr in s:
        for num in arr:
            if int(num) not in answer:
                answer.append(int(num))
    
    return answer