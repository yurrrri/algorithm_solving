def solution(participant, completion):
    dic = {}
    for part in participant:
        if part not in dic.keys():
            dic[part] = 1
        else:
            dic[part] += 1
                    
    for c in completion:
        dic[c] -= 1
                
    for key, value in dic.items():
        if value != 0:
            return key

# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)  # value가 0인 key-value쌍 제거되어 반환
#     print(list(answer.values()))
#     return list(answer.keys())[0]
