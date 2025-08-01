n, m, k = map(int, input().split())
money = [0] + list(map(int, input().split()))
answer = 0
parent = [i for i in range(n+1)]

def find(x):
  if parent[x] == x:
    return x

  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  root_x = find(x)
  root_y = find(y)
  
  if money[root_x] > money[root_y]:
    parent[root_x] = root_y
  else:
    parent[root_y] = root_x

for _ in range(m):
  v, w = map(int, input().split())
  union(v, w)

for i in range(1, n+1):
    if i == find(i):
        answer += money[i]
    
if answer <= k:
  print(answer)
else:
  print("Oh no")