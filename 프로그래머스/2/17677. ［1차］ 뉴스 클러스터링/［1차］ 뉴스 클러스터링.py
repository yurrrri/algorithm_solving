from collections import Counter

def solution(str1, str2):
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    if not c1 and not c2:
        return 65536
    
    return int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
