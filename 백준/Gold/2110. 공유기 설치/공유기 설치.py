import sys

input = sys.stdin.readline
n, c = map(int, input().rstrip().split())  # 집의 개수, 공유기 개수
arr = []  # 집의 좌표
for _ in range(n):
  arr.append(int(input().rstrip()))
arr.sort()
answer = 0  # 가장 인접한 두 공유기 사이의 최대거리

start = 1
end = arr[-1] - arr[0]  # 거리의 최대값

while start <= end:
  mid = (start + end) // 2
  current = arr[0]
  count = 1 #공유기 개수

  for i in range(1, n): #앞에서부터 차근차근 설치 (0 자리는 이미 설치했으므로 제외)
    if arr[i] >= current + mid: #집 간의 간격이 mid 이상이라면 (최소의 최대값이 mid니까)
      count += 1
      current = arr[i] #그 다음 위치를 찾기 위해서 current를 i 위치로
              
  if count >= c: # 공유기를 c개 이상 설치할 수 있다면
    start = mid + 1
    answer = mid
  else:
    end = mid-1 #공유기 개수가 c 미만이라면 더 설치할 수 있도록 범위를 좁힘

print(answer)