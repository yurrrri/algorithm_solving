n = int(input())
arr = [0] + list(map(int, input().split()))

for i in range(1, n+1):
  for j in range(1, i+1):
    arr[i] = max(arr[i-j] + arr[j], arr[i])

print(arr[n])