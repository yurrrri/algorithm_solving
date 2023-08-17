import sys

n, c = map(int, sys.stdin.readline().rstrip().split())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr.sort() #이진탐색을 위해서 먼저 sort

start = 1
end = arr[-1] - arr[0] #집간의 가장 큰 간격
answer = 0

while start <= end:
  mid = (start + end) // 2
  current = arr[0]
  count = 1 #공유기 개수

  for i in range(1, n): #앞에서부터 차근차근 설치 (0 자리는 이미 설치했으므로 제외)
    if arr[i] >= current + mid: #집 간의 간격이 mid 이상이라면 (최소의 최대값이 mid니까)
      count += 1
      current = arr[i] #그 다음 위치를 찾기 위해서 current를 i 위치로
              
  if count >= c: 
    start = mid + 1
    answer = mid
  else:
    end = mid-1 #공유기 개수가 c 미만이라면

print(answer)