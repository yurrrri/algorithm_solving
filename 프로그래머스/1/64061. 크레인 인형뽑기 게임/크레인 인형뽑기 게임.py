def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    
    for num in moves:
        for i in range(n):
            if board[i][num-1] != 0:
                if stack and stack[-1] == board[i][num-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(board[i][num-1])
                board[i][num-1] = 0
                break
    return answer