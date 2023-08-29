from collections import Counter

def solution(str1, str2):
    answer = 0 # 나중에 65536 곱한 후에 소수점 아래 버린 정수부 출력
    str1 = str1.upper()  # 대문자와 소문자 차이를 무시하기 위해 대문자로 통일
    str2 = str2.upper()
    
    if str1 == str2:
        return 65536
        
    s1 = []
    s2 = []
    
    len1 = 0
    len2 = 0 
    
    for i in range(len(str1)):
        if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2 and ' ' not in str1[i:i+2]:
            s1.append(str1[i:i+2])
        
    for j in range(len(str2)):
        if str2[j:j+2].isalpha() and len(str2[j:j+2]) == 2 and ' ' not in str2[j:j+2]:
            s2.append(str2[j:j+2])
            
    dic1 = Counter(s1)
    dic2 = Counter(s2)
    
    for key, value in dic1.items():
        if key in dic2:
            len1 += min(value, dic2[key])
            len2 += max(value, dic2[key])
        else:
            len2 += dic1[key]
            
    for key, value in dic2.items():
        if key not in dic1:
            len2 += dic2[key]
    
    return int(len1/len2 * 65536)

# 다른 풀이
def solution(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    
    return answer
        