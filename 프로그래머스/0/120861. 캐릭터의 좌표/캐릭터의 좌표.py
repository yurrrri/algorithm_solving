def solution(keyinput, board):
    dic = {"left": [-1, 0], "right": [1, 0], "up": [0, 1], "down": [0, -1]}
    n = board[0]
    m = board[1]
    
    def isValid(x, y):
        return -n/2 <= x <= n/2 and -m/2 <= y <= m/2
    
    x = 0
    y = 0
    
    for key in keyinput:
        nx = x + dic[key][0]
        ny = y + dic[key][1]
                
        if isValid(nx, ny):
            x = nx
            y = ny
            
    return [x, y]