import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

if k < 5:
  print(0)
  exit(0)
elif k == 26:
  print(n)
  exit(0)

arr = []
for _ in range(n):
  read = input().rstrip()
  arr.append(read)
answer = 0

visited = [False] * 26
# 적어도 언어 하나는 배우기위해 a,c,i,n,t 는 무조건 배워야함
for c in ('a', 'c', 'i', 'n', 't'):
  visited[ord(c) - ord('a')] = 1

def countComposedOfStr():
  count = 0
  for word in arr:
    count += 1
    for w in word:
      if not visited[ord(w) - ord('a')]:
        count -=1
        break
        
  return count

def dfs(idx, count):
  global answer

  if count == k-5:
    answer = max(answer, countComposedOfStr())
    return

  for i in range(idx, 26):
    if not visited[i]:
      visited[i] = True
      dfs(i, count+1)
      visited[i] = False

dfs(0, 0)
print(answer)