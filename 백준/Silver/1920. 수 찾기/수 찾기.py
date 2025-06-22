n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
haveToFind = list(map(int, input().split()))

def binarySearch(num):
  start = 0
  end = n-1

  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == num:
      return 1
    elif arr[mid] > num:
      end = mid - 1
    else:
      start = mid + 1

  return 0

for num in haveToFind:
  print(binarySearch(num))