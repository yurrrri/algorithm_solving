n, m = map(int, input().split())
know_persons = list(map(int, input().split()))
parties = []
for _ in range(m):
  parties.append(list(map(int, input().split())))

if know_persons[0] == 0:
  print(m)
  exit()

parent = [i for i in range(n+1)]

def find(x):
  if parent[x] == x:
    return x

  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  root_x = find(x)
  root_y = find(y)

  if root_x < root_y:
      parent[root_y] = root_x
  else:
      parent[root_x] = root_y

for i in range(m):
  party_persons = parties[i][1:]
  n = len(party_persons)

  for j in range(n-1):
    union(party_persons[j], party_persons[j+1])

result = 0
for i in range(m):
  possible = True
  first = parties[i][1]

  for j in range(1, len(know_persons)):
    if (find(first) == find(know_persons[j])):
      possible = False
      break

  if possible:
      result += 1

print(result)