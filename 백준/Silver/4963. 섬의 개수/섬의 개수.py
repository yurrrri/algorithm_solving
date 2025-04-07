import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y, graph, visited, len_x, len_y):
  visited[x][y] = True

  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<len_x and 0<=ny<len_y and not visited[nx][ny] and graph[nx][ny] == 1:
      dfs(nx, ny, graph, visited, len_x, len_y)

w, h = map(int, input().split())
while w != 0 and h != 0:
  graph = []
  answer = 0
  
  for _ in range(h):
    graph.append(list(map(int, input().split())))
  visited = [[False] * w for _ in range(h)]

  for i in range(h):
    for j in range(w):
      if not visited[i][j] and graph[i][j]:
        dfs(i, j, graph, visited, h, w)
        answer += 1

  print(answer)

  w, h = map(int, input().split())