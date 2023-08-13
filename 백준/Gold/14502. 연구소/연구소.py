import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0 #안전영역의 최대값
zeroArr = []
q = deque()

for _ in range(n):
  board.append(list(map(int, input().rstrip().split())))

for i in range(n):
  for j in range(m):
    if board[i][j] == 2:  #바이러스 있는 위치 큐에 삽입
      q.append((i, j))
    elif board[i][j] == 0:
      zeroArr.append((i, j))

def countSafeArea(board): # 안전구역 개수세기
  count = 0
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 0:
        count += 1

  return count

def bfs(q, board):
  while q:
    x, y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0<=nx<n and 0<=ny<m and not board[nx][ny]:  # 0이면
        board[nx][ny] = 2 #바이러스 감염 후 큐에 삽입
        q.append((nx, ny))

combi = combinations(zeroArr, 3)
for i in combi:
  for x, y in i:
    board[x][y] = 1
  copiedBoard = copy.deepcopy(board)
  copiedQ = q.copy()
  bfs(copiedQ, copiedBoard)
  answer = max(countSafeArea(copiedBoard), answer)

  for x, y in i:
    board[x][y] = 0
print(answer)