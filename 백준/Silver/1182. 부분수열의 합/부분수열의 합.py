import sys

input = sys.stdin.readline
n, s = map(int, input().rstrip().split())
board = list(map(int, input().rstrip().split()))
answer = 0

def dfs(idx, sum):
  global answer
  
  if idx > 0 and sum == s:
    answer += 1

  for i in range(idx, n):
    dfs(i+1, sum + board[i])

dfs(0, 0)
print(answer)