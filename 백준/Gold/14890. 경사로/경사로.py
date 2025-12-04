n, l = map(int, input().split())   # l: 경사로의 길이, 갯수 무제한
board = []
for i in range(n):
  board.append(list(map(int, input().split())))
answer = 0
    
# 경사로를 놓음으로서 길을 만들 수 있는지 판단하는 함수
# 경사로를 놓은 곳에 또 경사로를 놓는 경우 -> False
# 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우 -> False
# 낮은 지점의 칸의 높이가 모두 같지 않거나, L개 연속 X -> False
def can_install(road):
  visited = [False] * n   # 경사로 설치 여부를 판단하는 배열
  if len(set(road)) == 1:  # 모두 같은 숫자로 이루어져있는 경우, 길이므로 바로 return True
    return True

  for i in range(1, n):
    diff = road[i-1] - road[i]
    if abs(diff) > 1:   # 낮은 칸과 높은 칸의 차이가 1보다 크다면, 경사로를 놓을 수 없음 -> 길이 될 수 없음
      return False

    if diff == -1:    # 좌측으로 경사로 놓기
      for j in range(l):
        if i-1-j < 0:   # 범위를 벗어나 경사로를 놓을 수 없는 경우 
          return False
        if visited[i-1-j]: # 이미 경사로를 놓은 경우
          return False
        if road[i-1] != road[i-1-j]:
          return False
        visited[i-1-j] = True
    elif diff == 1:     # 우측으로 경사로 놓기
      for j in range(l):
        if i + j >= n:   # 범위를 벗어나 경사로를 놓을 수 없는 경우 
          return False
        if visited[i+j]: # 이미 경사로를 놓은 경우
          return False
        if road[i] != road[i+j]:
          return False
        visited[i+j] = True

  return True
for i in range(n):
  row = board[i]               # i번째 가로줄
  col = [board[r][i] for r in range(n)]  # i번째 세로줄
  # 가로
  if can_install(row):   # 길이 될 수 있으면
    answer += 1
  # 세로
  if can_install(col):   # 길이 될 수 있으면
    answer += 1

print(answer)