# def solution(numbers, hand):
#     answer = ''
#     left, right = 10, 12    # *을 10, #을 12로 치환
#     for i in range(len(numbers)):
#         if numbers[i] == 0:
#             numbers[i] = 11
    
#     for n in numbers:
#         if n in [1, 4, 7]:
#             answer += "L"
#             left = n
#         elif n in [3, 6, 9]:
#             answer += "R"
#             right = n
#         elif n in [2, 5, 8, 11]:
#             left_dist = (abs(n - left) // 3) + abs(n - left) % 3
#             right_dist = (abs(n - right) // 3) + abs(n - right) % 3
#             if left_dist < right_dist:
#                 left = n
#                 answer += "L"
#             elif left_dist > right_dist:
#                 right = n
#                 answer += "R"
#             else:
#                 if hand == "left":
#                     left = n
#                     answer += "L"
#                 else:
#                     right = n
#                     answer += "R"
                    
#     return answer

def solution(numbers, hand):
    answer = ''
    key_dic = {1: (0, 0), 2: (0, 1), 3: (0, 2),
               4: (1, 0), 5: (1, 1), 6: (1, 2),
               7: (2, 0), 8: (2, 1), 9: (2, 2), 
               0: (3, 1)}
    left_pos, right_pos = (3, 0), (3, 2)
    
    for n in numbers:
        if n in [1, 4, 7]:
            answer += "L"
            left_pos = key_dic[n]
        elif n in [3, 6, 9]:
            answer += "R"
            right_pos = key_dic[n]
        elif n in [2, 5, 8, 0]:
            left_dist = abs(key_dic[n][0] - left_pos[0]) + abs(key_dic[n][1] - left_pos[1])
            right_dist = abs(key_dic[n][0] - right_pos[0]) + abs(key_dic[n][1] - right_pos[1])
            if left_dist < right_dist:
                left_pos = key_dic[n]
                answer += "L"
            elif left_dist > right_dist:
                right_pos = key_dic[n]
                answer += "R"
            else:
                if hand == "left":
                    left_pos = key_dic[n]
                    answer += "L"
                else:
                    right_pos = key_dic[n]
                    answer += "R"
                    
    return answer