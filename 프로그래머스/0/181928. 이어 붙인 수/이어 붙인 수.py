def solution(num_list):
    num1 = "".join([str(i) for i in num_list if i%2 != 0])
    num2 = "".join([str(i) for i in num_list if i%2 == 0])
    return int(num1) + int(num2)