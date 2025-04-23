import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []
maxHeight = -1

for _ in range(n):
  arr = list(map(int, input().split()))
  maxHeight = max(maxHeight, max(arr))
  graph.append(arr)

def dfs(x, y):
  visited[x][y] = True

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] > height:
      dfs(nx, ny)

answer = 0
for height in range(maxHeight+1):
  visited = [[False] * n for _ in range(n)]
  area_count = 0

  for x in range(n):
    for y in range(n):
      if graph[x][y] > height and not visited[x][y]:
        dfs(x, y)
        area_count += 1

  answer = max(answer, area_count)

print(answer)