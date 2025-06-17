def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)
    
    for num in moves:
        for i in range(n):
            if board[i][num-1]:   # 크레인에서 인형 찾음
                if stack and stack[-1] == board[i][num-1]:  # 같으면 터뜨림
                    answer += 2     # 인형이 함께 엎어지니까 + 2
                    stack.pop()
                else:
                    stack.append(board[i][num-1])    # 그 앞에있는 인형과 다르니까 추가함
                board[i][num-1] = 0   # 뽑았으므로 0으로 만들되, 그 이후로는 넘어가지 않아야하니까
                break      # break로 반복문 멈춤
    return answer