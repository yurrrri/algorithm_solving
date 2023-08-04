def solution(array, height):
    answer = 0
    return len([i for i in array if i > height])