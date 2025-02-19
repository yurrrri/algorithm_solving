def solution(num_str):
    answer = list(map(lambda x:int(x), list(num_str)))
    return sum(answer)