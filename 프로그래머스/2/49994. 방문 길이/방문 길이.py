def is_valid_move(x, y):    # 위치를 벗어나지 않는지 확인
    return -5 <= x <= 5 and -5 <= y <= 5

def solution(dirs):
    answer = set() # 중복 제거
    x, y = 0, 0  # 시작위치 지정
    direction = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    
    for dir in dirs:
        nx , ny = x + direction[dir][0], y + direction[dir][1]
            
        if not is_valid_move(nx, ny):
            continue
            
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        
        x, y = nx, ny   # 그 다음 좌표로 이동
        
    return len(answer)/2