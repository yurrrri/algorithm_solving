from collections import Counter

def solution(nums):
    dic = Counter(nums)
    
    # for key, value in dic.items():
    #     print(f"{key} {value}")
        
    return min(len(list(dic.keys())), len(nums)/2)