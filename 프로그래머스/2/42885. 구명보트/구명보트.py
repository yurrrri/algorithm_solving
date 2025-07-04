def solution(people, limit):
    answer = 0
    people.sort()
    
    i, j = 0, len(people)-1        # 가장 가벼운 사람, 무거운 사람을 가리키는 인덱스
    while i <= j:
        if people[i] + people[j] <= limit:    # 가장 가벼운 사람과 무거운 사람을 같이 태울 수 있으면
            i += 1
        answer += 1                         # 그렇지 않으면 무거운 사람만 태움
        j -= 1
            
    return answer