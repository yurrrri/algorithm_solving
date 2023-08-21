from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
target = 0 #반복문바다 바뀔 타겟
operators = ["D", "S", "L", "R"]
visited = [False] * 10000

def transfer(n, op):
  if op == "D":
    n*=2
    return n%10000
  elif op == "S":
    return (n-1)%10000
  elif op == "L":   # deque.rotate(): 시간초과 주범
    return (n // 1000 + (n % 1000) * 10)
  else:
    return (n // 10 + (n % 10) * 1000)

def bfs(num):
  global target
  
  q = deque([(num, "")])
  visited[num] = True
  idx = 0

  while idx < len(q):
    n, regi = q[idx]

    if n == target:
      print(regi)
      break

    for i in range(4):
      transformed = transfer(n, operators[i])
      
      if not visited[transformed]:
        visited[transformed] = True
        q.append((transformed, regi + operators[i]))

    idx += 1
  
for _ in range(n):
  a, target = map(int, input().rstrip().split())
  visited = [False] * 10000
  bfs(a)