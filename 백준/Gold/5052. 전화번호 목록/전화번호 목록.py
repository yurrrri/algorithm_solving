from collections import defaultdict

t = int(input())
for _ in range(t):
  dic = defaultdict(int)
  words = set()
  flag = False
  n = int(input())
  for _ in range(n):
    number = input()
    words.add(number)
    for i in range(1, len(number)+1):
      dic[number[:i]] += 1
  
  for (k, v) in dic.items():
    if k in words and v>=2:
        print("NO")
        flag = True
        break

  if not flag:
    print("YES")