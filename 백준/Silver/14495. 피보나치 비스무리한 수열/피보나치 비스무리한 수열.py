n = int(input())
arr = [1] * (n+3)

if 1<=n and n<=3:
  print(1)
else:
  for i in range(4, n+1):
    arr[i] = arr[i-1] + arr[i-3]
  print(arr[n])