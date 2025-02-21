def solution(arr, queries):
    answer = []
    for a, b, c in queries:
        temp = [i for i in arr[a:b+1] if i > c]
        answer.append(-1 if len(temp) == 0 else min(temp))
    return answer