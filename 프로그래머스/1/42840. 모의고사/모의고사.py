def solution(answers):
    first_student = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    second_student = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    student_score_list = [0] * 3
    
    answer = []
    
    for i, score in enumerate(answers):
        if first_student[i] == score:
            student_score_list[0] += 1
        if second_student[i] == score:
            student_score_list[1] += 1
        if third_student[i] == score:
            student_score_list[2] += 1
            
    answer = [i+1 for i, total in enumerate(student_score_list) if total == max(student_score_list)]
    return answer