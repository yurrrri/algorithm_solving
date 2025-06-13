def solution(people, limit):
    if len(people) == 1:
        return 1
    
    people.sort()
    answer = 0
    i = 0   # 가장 가벼운 사람을 가리키는 인덱스
    j = len(people) - 1   # 가장 무거운 사람을 가리키는 인덱스
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        answer += 1
        j -= 1
            
    return answer