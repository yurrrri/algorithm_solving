def solution(answers):
    first_student = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    second_student = [2, 1, 2, 3, 2, 4, 2, 5] * (len(answers)//8 + 1)
    third_student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    student_score_list = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if first_student[i] == answers[i]:
            student_score_list[0] += 1
        if second_student[i] == answers[i]:
            student_score_list[1] += 1
        if third_student[i] == answers[i]:
            student_score_list[2] += 1
            
    max_num = max(student_score_list)
    answer = [i+1 for i in range(3) if student_score_list[i] == max_num]
    return answer