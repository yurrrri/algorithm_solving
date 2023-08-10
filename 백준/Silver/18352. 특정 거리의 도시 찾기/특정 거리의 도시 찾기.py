import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

q = deque([x])
board = [[] for _ in range(n+1)] #n+1 개의 빈 리스트가 있는 배열 (인덱스가 아닌 노드의 수로 바로 넣기 위해)
visited = [-1] * (n+1)
visited[x] = 0

for _ in range(m):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  board[x].append(y)

while q:
  a = q.popleft()
  for i in board[a]:
    if visited[i] == -1: #방문 안한 노드
      visited[i] = visited[a] + 1
      q.append(i)

satisfy = False

for i in range(1, n+1):
  if visited[i] == k:
    print(i)
    satisfy = True


if satisfy == False:
  print(-1)