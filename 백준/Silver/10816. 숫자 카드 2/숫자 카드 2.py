from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
counter = Counter(arr)
m = int(input())
haveToFind = list(map(int, input().split()))

for num in haveToFind:
  if num not in counter:
    print(0, end=" ")
  else:
    print(counter[num], end=" ")