from collections import Counter

n, d = map(int, input().split())
arr = []
for i in range(1, n+1):
  arr.extend(map(int, list(str(i))))

print(Counter(arr)[d])