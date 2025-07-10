def solution(numbers, hand):
    answer = ''
    left, right = 10, 12    # *을 10, #을 12로 치환
    for i in range(len(numbers)):
        if numbers[i] == 0:
            numbers[i] = 11
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            left = n
        elif n in [3, 6, 9]:
            answer += "R"
            right = n
        elif n in [2, 5, 8, 11]:
            left_dist = (abs(n - left) // 3) + abs(n - left) % 3
            right_dist = (abs(n - right) // 3) + abs(n - right) % 3
            if left_dist < right_dist:
                left = n
                answer += "L"
            elif left_dist > right_dist:
                right = n
                answer += "R"
            else:
                if hand == "left":
                    left = n
                    answer += "L"
                else:
                    right = n
                    answer += "R"
                    
        
        
    return answer