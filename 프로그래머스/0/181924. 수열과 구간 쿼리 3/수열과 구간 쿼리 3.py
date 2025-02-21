def solution(arr, queries):
    answer = arr
    for q in queries:
        a = answer[q[1]]
        answer[q[1]] = answer[q[0]]
        answer[q[0]] = a
    return answer