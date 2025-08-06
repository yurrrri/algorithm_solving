from collections import defaultdict, Counter

def solution(points, routes):
    dic = defaultdict(list)
    answer = 0
    
    for route in routes:
        time = 0
        from_x, from_y = points[route[0]-1][0], points[route[0]-1][1]
        dic[time].append((from_x, from_y))

        for i in range(1, len(route)):
            to_x, to_y = points[route[i]-1][0], points[route[i]-1][1]

            # r 좌표 우선 이동
            while from_x != to_x:
                time += 1
                from_x += 1 if from_x < to_x else -1
                dic[time].append((from_x, from_y))

            # c 좌표 이동
            while from_y != to_y:
                time += 1
                from_y += 1 if from_y < to_y else -1
                dic[time].append((from_x, from_y))
                
    for v in dic.values():
        counter = Counter(v)
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1
            
    return answer