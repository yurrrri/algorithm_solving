import copy

n, m = map(int, input().split())  # mxn 크기의 보드
board = []
for _ in range(n):
  board.append(list(input()))
  
answer = int(1e9)

def simulation(x, y, board):  # 8x8 함수에서 칠해야하는 정사각형의 갯수 구하는 함수
  w_index=0 #흰색으로 시작
  b_index=0 #검은색으로 시작
  for i in range(x,x+8):#시작지점
    for j in range(y,y+8):#시작지점
      if (i+j)%2==0:#짝수인 경우
        if board[i][j] == "B":# B이면
          w_index+=1#W로 칠하는 갯수
        else:#W일 때
          b_index+=1#B로 칠하는 갯수
      else:#홀수인 경우
        if board[i][j] == "B" :# B이면
          b_index+=1#B로 칠하는 갯수
        else:
          w_index+=1#W로 칠하는 갯수

  return min(w_index, b_index)

for i in range(n-7):
  for j in range(m-7):
    answer = min(answer, simulation(i, j, board))

print(answer)