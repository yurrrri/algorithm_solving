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
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque([(0, 0, 0)])
  visited[0][0][0] = 1  # 2) 부수지 않은 경우부터 시작

  while q:
    x, y, wall = q.popleft()
    if x == n - 1 and y == m - 1:
        return visited[x][y][wall]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 만약 20번째줄의 wall 평행세계?가 방문하지 않은 상황이라면, 벽을 부순 경우와 부수지 않은 경우를 나누어 큐에 저장 및 visited 처리한다.

      if 0<=nx<n and 0<=ny<m and not visited[nx][ny][wall]:
        if board[nx][ny] == 0:  # 벽이 아닌 통과할 수 있는 곳이라면 원래대로
            q.append((nx, ny, wall))
            visited[nx][ny][wall] = visited[x][y][wall] + 1

        # 다음 탐색 노드가 벽인 상황에서 wall이 0이라면 부술 수 있으므로 3차원의 데이터를 1로 하여 저장함
        if board[nx][ny] == 1 and wall == 0:
          q.append((nx, ny, 1))
          visited[nx][ny][1] = visited[x][y][wall] + 1

  return -1

print(bfs())