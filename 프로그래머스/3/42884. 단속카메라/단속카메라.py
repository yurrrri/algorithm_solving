def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 0
    prev_end = -30001
    for start, end in routes :
        if start > prev_end :
            answer += 1
            prev_end = end

    return answer