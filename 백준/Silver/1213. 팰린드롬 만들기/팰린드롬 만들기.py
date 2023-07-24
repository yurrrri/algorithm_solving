from collections import Counter

str = input()
counter = Counter(str)

mid = ''
oddCount = 0

for k, v in list(counter.items()):
  if v%2 != 0:
    mid = k
    oddCount += 1

  if oddCount >= 2:
    print("I'm Sorry Hansoo")
    exit(0)

result = ''

arr = sorted(counter.items())
for k, v in arr:
  result += k * (v//2)

result += mid + result[::-1]
print(result)