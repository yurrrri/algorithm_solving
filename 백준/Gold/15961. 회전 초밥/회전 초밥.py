import sys
from collections import defaultdict

# 투포인터로 접근
n, d, k, c = map(int, sys.stdin.readline().rstrip().split()) # c: 쿠폰번호
sushi = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dic = defaultdict(int)
dic[c] = 1 # 최대값 --> 쿠폰에 있는 초밥은 무조건 먹기

start = 0
end = 0
while end < k:  # 맨 처음 연속된 k개의 초밥 포함
  dic[sushi[end]] += 1
  end += 1
answer = 0
end -= 1

while start < n:   # end < n으로 하면 맨 마지막 후보를 비교하지 못하므로 <=n으로 해두고, 중간에 이동할때 멈춰줌
  answer = max(len(dic), answer)  # list(dic)은 매우 느림
  dic[sushi[start]] -= 1   # 옆으로 이동하기 위해 현재의 start는 빼주고
  if dic[sushi[start]] == 0:
    del dic[sushi[start]]
    
  start += 1
  end += 1
  dic[sushi[end%n]] += 1

print(answer)