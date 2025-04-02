def solution(wallpaper):
    board_x_length = len(wallpaper)
    board_y_length = len(wallpaper[0])
    answer = [51, 51, 0, 0]
    
    for x in range(board_x_length):
        for y in range(board_y_length):
            if wallpaper[x][y] == "#":
                answer[0] = min(answer[0], x)
                answer[1] = min(answer[1], y)
                answer[2] = max(answer[2], x+1)   # 드래그하는 범위이므로 각각 + 1
                answer[3] = max(answer[3], y+1)
    
    return answer