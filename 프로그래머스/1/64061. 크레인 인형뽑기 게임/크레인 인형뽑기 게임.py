def solution(board, moves):
    answer = 0
    stack = []     # 인형을 놓을 스택
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                if stack and stack[-1] == board[i][m-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
                
    return answer