from collections import Counter
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
  word = input().rstrip()
  if len(word) < m:
    continue

  arr.append(word)

counter = Counter(arr)
arr = set(arr)
arr = list(arr)

arr = sorted(arr, key=lambda x:(-counter[x], -len(x), x))
print("\n".join(arr))