import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())

#남극 언어의 모든 단어는 anta, tica로 끝남. 즉 최소 a, n, t, i, c 5개는 배워야만 1개 이상의 단어를 배울 수 있음
if k < 5:   # 5개 미만으로 배우면 1개의 단어도 읽을 수 없음
  print(0)
  exit(0)
elif k == 26:  # 26개의 단어를 배울 수 있으면 모든 단어를 알 수 있음
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
      if not visited[ord(w) - ord('a')]: #배우지 않은 단어가 있다면 못읽음 --> break
        count -=1
        break
        
  return count

def dfs(idx, count):
  global answer

  if count == k-5:  # a, n, t, i, c을 제외한 알파벳 중 다른 단어를 더 배웠다면
    answer = max(answer, countComposedOfStr())
    return

  for i in range(idx, 26):
    if not visited[i]:
      visited[i] = True
      dfs(i+1, count+1)
      visited[i] = False

dfs(0, 0)
print(answer)