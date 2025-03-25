def isEmpty(stack):
    return len(stack) == 0

def solution(board, moves):
    answer = 0
    board_size = len(board)
    stack = []
    
    for move in moves:
        for i in range(board_size):
            doll = board[i][move-1]  # 인형 찾아서
            board[i][move-1] = 0    # 꺼냄
            if doll != 0:   # 인형 찾음, 없는 곳에서 크레인을 작동시키면 아무일도 일어나지 않음
                if not isEmpty(stack) and stack[-1] == doll:
                    answer += 1
                    stack.pop()
                else:
                    stack.append(doll)
                break
                 
    return answer * 2