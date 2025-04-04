import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = list(map(int, input().split()))
sliding_window = sum(arr[:k])
answer = sliding_window

for i in range(1, n-k+1):
  sliding_window -= arr[i-1]
  sliding_window += arr[i+k-1]
  answer = max(answer, sliding_window)

print(answer)