def solution(a, d, included):
    answer = 0
    num_list = [a + d*i for i in range(len(included))]
    for idx in range(len(included)):
        if included[idx]:
            answer += num_list[idx]
    return answer