from collections import Counter

def solution(str1, str2):
    answer = 0
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[j:j+2].lower() for j in range(len(str2)-1) if str2[j:j+2].isalpha()]

    if not s1 and not s2:
        return 65536
            
    dic1 = Counter(s1)
    dic2 = Counter(s2)
    
    return int(sum((dic1 & dic2).values()) / sum((dic1 | dic2).values()) * 65536)