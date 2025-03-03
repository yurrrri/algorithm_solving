def is_valid_move(x, y):    # 위치를 벗어나지 않는지 확인
    return -5 <= x <= 5 and -5 <= y <= 5

def solution(dirs):
    answer = set()
    x, y = 0, 0  # 시작위치 지정
    
    for dir in dirs:
        if dir == "U":
            nx, ny = x, y + 1
        elif dir == "D":
            nx, ny = x, y - 1
        elif dir == "R":
            nx, ny = x + 1, y
        else:
            nx, ny = x - 1, y
            
        if not is_valid_move(nx, ny):
            continue
            
        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))
        
        x, y = nx, ny
        
    return len(answer)/2