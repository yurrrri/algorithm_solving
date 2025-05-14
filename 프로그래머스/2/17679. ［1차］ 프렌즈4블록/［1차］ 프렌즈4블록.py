def solution(m, n, board):
    answer = 0
    board = [list(i) for i in board]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def down():
        for y in range(n):
            for i in range(m-2, -1, -1):
                for x in range(m-1, i, -1):
                    if board[i][y] != "." and board[x][y] == ".":
                        board[x][y] = board[i][y]
                        board[i][y] = "."
    
    while True:
        pop_set = set()

        # 1. 2x2 같은 블록 찾기
        for i in range(m):
            for j in range(n):
                if not (0<=i+1<m and 0<=j+1<n):
                    continue
                if board[i][j] == ".":
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    pop_set.update([(i, j), (i+1, j), (i, j+1), (i+1, j+1)])

        # 2. 제거 없으면 종료
        if not pop_set:
            break
        answer += len(pop_set)

        # 3. 제거
        for x, y in pop_set:
            board[x][y] = "."
            
        down()
            
    return answer