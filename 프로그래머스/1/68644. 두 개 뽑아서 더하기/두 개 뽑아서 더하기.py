def solution(numbers):
    answer = []
    num = len(numbers)
    for i in range(num-1):
        for j in range(i+1, num):
            answer.append(numbers[i] + numbers[j])
            
    return sorted(list(set(answer)))