def solution(commands):
    answer = []
    pyo = [["EMPTY"] * 51 for _ in range(51)]   # 50x50 고정, 비어있는 셀을 "EMPTY"로 표현한다.
    merged = [[(i, j) for j in range(51)] for i in range(51)]   # 병합된 좌표들을 저장하는 배열. 초기에는 자기 자신의 좌표로 초기화함
    
    for c in commands:
        command = c.split()
        if command[0] == "UPDATE":
            if len(command) == 4:    # 길이가 4인 경우 (r, c) 위치가 주어짐
                r, c, value = int(command[1]), int(command[2]), command[3]
                x, y = merged[r][c]   # 병합된 좌표값 얻어오기
                pyo[x][y] = value
            else:
                value1, value2 = command[1], command[2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if pyo[i][j] == value1:
                            pyo[i][j] = value2
                
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            x1, y1 = merged[r1][c1]
            x2, y2 = merged[r2][c2]
            if pyo[x1][y1] == "EMPTY":
                value = pyo[x2][y2]
                
                for i in range(1, 51):
                    for j in range(1, 51):
                        if merged[i][j] == (x1, y1):
                            merged[i][j] = (x2, y2)
                            pyo[i][j] = value
                pyo[x1][y1] = value
                            
            else:
                value = pyo[x2][y2]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if merged[i][j] == (x2, y2):
                            merged[i][j] = (x1, y1)
                            pyo[i][j] = value
                pyo[x2][y2] = value

        elif command[0] == "UNMERGE":
            r, c = int(command[1]), int(command[2])
            x, y = merged[r][c]
            temp = pyo[x][y]
            for i in range(1, 51):
                for j in range(1, 51):
                    if merged[i][j] == (x, y):
                        merged[i][j] = (i, j)
                        pyo[i][j] = "EMPTY"
            pyo[r][c] = temp
        else:    # PRINT -> answer 배열에 추가
            r, c = int(command[1]), int(command[2])
            x, y = merged[r][c]
            answer.append(pyo[x][y])
            
    return answer