from collections import deque

n, m, k = map(int, input().split())
# nxn 크기의 땅
board = [[5] * n for _ in range(n)]
A = []  # 겨울에 추가되는 양분의 양
trees = [[deque() for _ in range(n)] for _ in range(n)]  # 각 칸마다의 나무 나이, 여러 개의 나무가 있을 수도 있다
for _ in range(n):
  A.append(list(map(int, input().split())))
for _ in range(m):
  x, y, z = map(int, input().split())
  trees[x-1][y-1].append((z, False))
for i in range(n):
  for j in range(n):
    if trees[i][j]:
      trees[i][j] = deque(sorted(trees[i][j]))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(k):
  # 봄
  for i in range(n):
    for j in range(n):
      if trees[i][j]:
        temp = deque([])
        for age, isDead in trees[i][j]:    # 나이가 어린 나무부터 양분을 먹기 위해 정렬
          if not isDead:
            if board[i][j] < age: # 양분 부족
              temp.append((age, True))
            else:
              board[i][j] -= age  # 나이만큼의 양분을 먹고, 나이 1 증가
              temp.append((age+1, False))

        trees[i][j] = temp
  
  # 여름
  for i in range(n):
    for j in range(n):
      if trees[i][j]:
        for age, isDead in trees[i][j]:
          if isDead:   # 죽은 나무인 경우에만 양분 추가
            board[i][j] += age // 2
  
  # 가을
  for x in range(n):
    for y in range(n):
      if trees[x][y]:
        for age, isDead in trees[x][y]:
          if age % 5 == 0 and not isDead:
            for l in range(8):
              nx = x + dx[l]
              ny = y + dy[l]

              if 0<=nx<n and 0<=ny<n:
                trees[nx][ny].appendleft((1, False))
  
  # 겨울
  for i in range(n):
    for j in range(n):
      board[i][j] += A[i][j]

answer = 0

for i in range(n):
  for j in range(n):
    if trees[i][j]:
      for _, isDead in trees[i][j]:
        if not isDead:
          answer += 1

print(answer)