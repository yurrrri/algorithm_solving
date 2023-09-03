import sys
input = sys.stdin.readline

def bisect(arr, n):
  start = 0
  end = len(arr)-1

  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == n:
      return 1
    elif arr[mid] > n:
      end = mid - 1
    else:
      start = mid + 1

  return 0

t = int(input().rstrip())
for _ in range(t):
  n = int(input().rstrip())
  note1 = list(map(int, input().rstrip().split()))
  note1.sort()

  m = int(input().rstrip())
  note2 = list(map(int, input().rstrip().split()))

  for i in note2:
    print(bisect(note1, i))