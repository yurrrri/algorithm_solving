n = int(input())
answer = 0
width = [False] * n
diagonal1 = [False] * (n * 2)
diagonal2 = [False] * (n * 2)

def backtracking(y):
  global answer
  
  if y == n:
    answer += 1
    return

  for i in range(n):
    if width[i] or diagonal1[i + y] or diagonal2[i - y + n]:
      continue

    width[i] = diagonal1[i+y] = diagonal2[i-y+n] = True
    backtracking(y+1)
    width[i] = diagonal1[i+y] = diagonal2[i-y+n] = False

backtracking(0)
print(answer)