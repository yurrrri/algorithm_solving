m, n = map(int, input().split())
arr = sorted(list(map(int, input().split())))
start, end = 1, arr[-1]
result = 0

while start <= end:
  mid = (start + end)//2
  cnt = 0
  for snack in arr:
    cnt += snack // mid

  if cnt >= m:
    result = mid
    start = mid + 1
  else:
    end = mid-1

print(result)