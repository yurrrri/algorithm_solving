from collections import defaultdict

def solution(str1, str2):
    answer = 0 # 나중에 65536 곱한 후에 소수점 아래 버린 정수부 출력
    str1 = str1.upper()  # 대문자와 소문자 차이를 무시하기 위해 대문자로 통일
    str2 = str2.upper()
    
    if str1 == str2:
        return 65536
        
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    
    len1 = 0
    len2 = 0 
    
    for i in range(len(str1)):
        if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2 and ' ' not in str1[i:i+2]:
            dic1[str1[i:i+2]] += 1
        
    for j in range(len(str2)):
        if str2[j:j+2].isalpha() and len(str2[j:j+2]) == 2 and ' ' not in str2[j:j+2]:
            dic2[str2[j:j+2]] += 1
            
    print(dic1)
    print(dic2)
    
    for key, value in dic1.items():
        if key in dic2:
            len1 += min(value, dic2[key])
            len2 += max(value, dic2[key])
        else:
            len2 += dic1[key]
            
    for key, value in dic2.items():
        if key not in dic1:
            len2 += dic2[key]
            
    # print(len1)
    # print(len2)
    
    return int(len1/len2 * 65536)
        