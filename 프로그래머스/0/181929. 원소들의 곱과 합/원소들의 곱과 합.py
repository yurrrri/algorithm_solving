def solution(num_list):
    num1 = 1
    for n in num_list:
        num1 *= n
    num2 = sum(num_list)**2
    return 1 if num1 < num2 else 0