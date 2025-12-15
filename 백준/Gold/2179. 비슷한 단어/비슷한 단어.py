from collections import defaultdict

dic = defaultdict(int)
n = int(input())
arr = []
for _ in range(n):
  word = input()
  arr.append(word)
  for i in range(len(word)+1):
    dic[word[:i]] += 1

answer = []
maxlen, maxprefix = 0, ""
for k, v in dic.items():
  if v >= 2 and maxlen < len(k):
    maxlen = len(k)
    maxprefix = k
    
for i, w in enumerate(arr):
  if maxprefix == w[:maxlen]:
    answer.append((w, i))
answer.sort(key=lambda x:x[1])

print(answer[0][0])
print(answer[1][0])