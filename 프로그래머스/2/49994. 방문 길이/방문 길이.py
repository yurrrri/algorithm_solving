def solution(dirs):
    answer = set()
    dirs = list(dirs)
    x, y = 0, 0
    
    for dir in dirs:
        cur_x, cur_y = x, y
        if dir == "U":
            y += 1
        elif dir == "L":
            x -= 1
        elif dir == "R":
            x += 1
        else:
            y -= 1
            
        if not (-5<=x<=5 and -5<=y<=5):
            x, y = cur_x, cur_y
        else:
            answer.add((cur_x, cur_y, x, y))
            answer.add((x, y, cur_x, cur_y))
            
    # print(answer)
            
    return len(answer)/2