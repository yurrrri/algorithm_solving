def solution(board, moves):
    # 0은 빈칸
    stack = []
    answer = 0
    board_size = len(board[0])
    
    for move in moves:
        for i in range(board_size):
            if board[i][move-1] != 0:
                if stack and stack[-1] == board[i][move-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
        
    return answer