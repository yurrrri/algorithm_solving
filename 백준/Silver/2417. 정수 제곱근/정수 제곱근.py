n = int(input())
answer = 0

def bfs(start, end):
  global answer
  
  while start <= end:
    mid = (start+end) // 2
    
    if mid**2 >= n:
      answer = mid
      end = mid-1
    else:
      start = mid+1

bfs(0, n)
print(answer)