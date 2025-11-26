n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 그리디를 풀때, 일단 후보지를 정렬한 다음에 문제를 풀 수 있는지 시도해보기
a.sort()
b.sort(reverse=True)
answer = 0

for i in range(n):      # 작은 순서대로x큰 순서대로 곱해서 더하기
  answer += a[i] * b[i]

print(answer)