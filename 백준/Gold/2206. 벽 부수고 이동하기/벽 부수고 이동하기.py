from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
"""
1)
벽을 부순 경우와 부수지 않은 경우를 3번째 인덱스에 저장하여 분기를 탐색하기 위해, 0의 원소 2개를 가지는 3차원 배열을 생성한다.
"""
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque([(0, 0, 0)])
  visited[0][0][0] = 1

  while q:
    x, y, wall = q.popleft()
    if x == n - 1 and y == m - 1:
        return visited[x][y][wall]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <=nx<n and 0<=ny<m and visited[nx][ny][wall] == 0:
        if board[nx][ny] == 0:
            q.append((nx, ny, wall))
            visited[nx][ny][wall] = visited[x][y][wall] + 1
          
        if wall == 0 and board[nx][ny] == 1:
          q.append((nx, ny, 1))
          visited[nx][ny][1] = visited[x][y][wall] + 1

  return -1

print(bfs())