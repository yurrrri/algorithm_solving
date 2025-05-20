def solution(n, build_frame):
    
    def isValid():
        for x, y in gidung:
            # 바닥 위에 있거나, 다른 기둥 위에 있거나, 보의 한쪽 끝부분에 있거나
            if not (y == 0 or (x, y-1) in gidung or (x-1, y) in bo or (x, y) in bo):
                return False

        for x, y in bo:
            # 한쪽 끝부분이 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 연결되어 있어야함
            if not ((x, y-1) in gidung or (x+1, y-1) in gidung or (x+1, y) in bo and (x-1, y) in bo):
                return False

        return True
    
    gidung = set()
    bo = set()
    
    for build in build_frame:
        # a: 0 기둥 1 보
        # b: 0 삭제 1 설치
        x, y, a, b = build
        
        if b == 1:
            if a == 0:
                gidung.add((x, y))
                if not isValid():
                    gidung.remove((x, y))
            else:
                bo.add((x, y))
                if not isValid():
                    bo.remove((x, y))
        else:
            if a == 0:
                gidung.remove((x, y))
                if not isValid():
                    gidung.add((x, y))
            else:
                bo.remove((x, y))
                if not isValid():
                    bo.add((x, y))    
    
    answer = []
    for x, y in gidung:
        answer.append([x, y, 0])
    for x, y in bo:
        answer.append([x, y, 1])
        
    return sorted(answer)