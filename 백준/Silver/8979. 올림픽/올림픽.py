n, k = map(int, input().split())
arr = []
idx = 0

for _ in range(n):
  num, gold, silver, bronze = map(int, input().split())
  arr.append([num, gold, silver, bronze])    
arr.sort(reverse=True, key=lambda x:(x[1], x[2], x[3]))

for i, a in enumerate(arr):
  if a[0] == k:
    idx = i
    break

for i, a in enumerate(arr):
  if a[1:] == arr[idx][1:]:
    print(i+1)
    break