from collections import Counter

def solution(str1, str2):
    answer = 0
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[j:j+2].lower() for j in range(len(str2)-1) if str2[j:j+2].isalpha()]

    bunja, bunmo = 0, 0
            
    dic1 = Counter(s1)
    dic2 = Counter(s2)
    
    for key, value in dic1.items():
        if key in dic2:
            bunja += min(value, dic2[key])
            bunmo += max(value, dic2[key])
        else:
            bunmo += dic1[key]
            
    for key, value in dic2.items():
        if key not in dic1:
            bunmo += dic2[key]
            
    if bunja == 0 and bunmo == 0:
        return 65536
    
    return int(bunja/bunmo * 65536)