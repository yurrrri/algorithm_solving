def is_valid(pillars, beams):
    for x, y in pillars:
        if y == 0 or (x, y-1) in pillars or (x-1, y) in beams or (x, y) in beams:
            continue
        return False

    for x, y in beams:
        if (x, y-1) in pillars or (x+1, y-1) in pillars or ((x-1, y) in beams and (x+1, y) in beams):
            continue
        return False

    return True

def solution(n, build_frame):
    pillars = set()
    beams = set()
    
    for x, y, a, b in build_frame:
        if a == 0:  # 기둥
            if b == 1:
                pillars.add((x, y))
                if not is_valid(pillars, beams):
                    pillars.remove((x, y))
            else:
                pillars.remove((x, y))
                if not is_valid(pillars, beams):
                    pillars.add((x, y))
        else:  # 보
            if b == 1:
                beams.add((x, y))
                if not is_valid(pillars, beams):
                    beams.remove((x, y))
            else:
                beams.remove((x, y))
                if not is_valid(pillars, beams):
                    beams.add((x, y))
    
    answer = []
    for x, y in pillars:
        answer.append([x, y, 0])
    for x, y in beams:
        answer.append([x, y, 1])
    
    return sorted(answer)