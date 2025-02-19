def solution(a, b):
    number1 = int(str(a) + str(b))
    number2 = 2 * a * b
    return number2 if number2 > number1 else number1