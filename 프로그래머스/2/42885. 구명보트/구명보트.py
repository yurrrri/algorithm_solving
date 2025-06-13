def solution(people, limit):
    if len(people) == 1:
        return 1
    
    people.sort()
    answer = 0
    i = 0   # 가장 가벼운 사람을 가리키는 인덱스
    j = len(people) - 1   # 가장 무거운 사람을 가리키는 인덱스
    
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1    # 무거운 사람과 가벼운 사람을 태울 수 있다면 가벼운 사람도 함께 태움
        answer += 1
        j -= 1      # 무거운 사람은 항상 보트에 탈 수 있으므로 태움
            
    return answer