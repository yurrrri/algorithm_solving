example = input()
n = len(example)
arr = [[0] * 26 for _ in range(n)]
arr[0][ord(example[0]) - ord('a')] = 1

for i in range(1, n):
  arr[i][ord(example[i]) - ord('a')] += 1
  for j in range(26):
    arr[i][j] += arr[i-1][j]

q = int(input())
for _ in range(q):
  alpha, start, end = input().split()
  start = int(start)
  end = int(end)
  
  if start == 0:
    print(arr[end][ord(alpha)-ord('a')])
  else:
    print(arr[end][ord(alpha)-ord('a')] - arr[start-1][ord(alpha)-ord('a')])