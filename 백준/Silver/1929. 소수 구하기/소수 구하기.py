import math

m, n = map(int, input().split())
arr = [True] * (n+1) # 소수인지 여부를 담을 배열 -> 처음엔 다 소수로 가정
arr[1] = False

for i in range(2, int(math.sqrt(n))+1):   # int(n**0.5) + 1
	if arr[i]:
		# i를 제외한 i의 모든 배수에 False 표시 (무언가의 배수이면 소수가 아님)
		j = 2
		while (i*j) <= n:
			arr[i*j] = False
			j += 1

for i in range(m, n+1): # 모든 소수 출력
	if arr[i]:   # 위 로직을 거쳐서 True인거라는거는 소수라는 의미임
		print(i)