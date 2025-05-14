def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def down():
        for y in range(n):
            for i in range(m-2, -1, -1):   # 아래
                for x in range(m-1, i, -1):   # 위
                    if board[i][y] != "." and board[x][y] == ".":
                        board[x][y] = board[i][y]
                        board[i][y] = "."
    
    while True:
        pop_set = set()   # 사라질때 겹치는 좌표가 있을 수 있으므로 중복 제거를 위해 set 사용

        # 1. 2x2 같은 블록 찾기
        for i in range(m):
            for j in range(n):
                if not (0<=i+1<m and 0<=j+1<n):
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] and board[i][j] != ".":
                    pop_set.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])

        # 2. 제거할 블록이 없으면 멈춤
        if not pop_set:
            break
        answer += len(pop_set)

        # 3. 제거
        for x, y in pop_set:
            board[x][y] = "."
            
        down()
            
    return answer