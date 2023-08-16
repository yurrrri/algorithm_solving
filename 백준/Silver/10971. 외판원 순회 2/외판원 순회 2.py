import sys

input = sys.stdin.readline
n = int(input().rstrip())
board = []
for _ in range(n):
  board.append(list(map(int, input().rstrip().split())))
visited = [False] * n #한번 갔던 도시로는 다시 갈 수 없다.
answer = int(1e9)
start = 0

def dfs(sum, depth, cur):  
  global answer
  
  if cur == start and depth == n: 
        #cur==start: 다시 돌아옴 depth==n: n개의 도시를 거침
    answer = min(answer, sum)
    return

  for i in range(n):
    if not visited[i] and board[cur][i] != 0:
      visited[i] = True
      dfs(sum + board[cur][i], depth+1, i)
      visited[i] = False

dfs(0, 0, 0)
print(answer)