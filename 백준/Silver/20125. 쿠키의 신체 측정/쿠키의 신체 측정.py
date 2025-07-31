n = int(input())
board = []
for _ in range(n):
  board.append(list(input()))

heart = (0, 0)
found = False
for i in range(n):
  for j in range(n):
    if board[i][j] == "*":
      heart = (i+1, j)
      found = True
      break

  if found:
    break
      
left_pal = 0
right_pal = 0
for j in range(n):
  if board[heart[0]][j] == "*":
    if j < heart[1]:
      left_pal += 1
    elif j > heart[1]:
      right_pal += 1

waist = 0
for i in range(heart[0]+1, n):
  if board[i][heart[1]] == "*":
    waist += 1
  else:
    break

left_leg = 0
right_leg = 0
for j in range(i, n):
  if board[j][heart[1]-1] == "*":
    left_leg += 1
  if board[j][heart[1]+1] == "*":
    right_leg += 1

print(heart[0]+1, heart[1]+1)
print(left_pal, right_pal, waist, left_leg, right_leg)