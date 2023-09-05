def solution(priorities, location):
    q = [(i, e) for i, e in enumerate(priorities)]
    answer = 0
    while True:
        i, e = q.pop(0)
        if any(e < a[1] for a in q):
            q.append((i, e))
        else:
            answer += 1
            if i == location:
                return answer