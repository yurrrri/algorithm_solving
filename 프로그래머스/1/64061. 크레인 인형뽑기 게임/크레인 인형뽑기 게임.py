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
                if not isEmpty(stack) and stack[-1] == doll: # 마지막께 넣는 인형이랑 같으면 터지고 갯수 더함
                    answer += 2   # 같이 없어지므로 + 2
                    stack.pop()
                else:    # 그게 아니면 인형 계속 추가하기
                    stack.append(doll)
                break     # 0이 아닌 인형을 찾으면 그 인형만 가지고 그 다음 스텝으로 넘어가야하므로 반복문 벗어남
                 
    return answer