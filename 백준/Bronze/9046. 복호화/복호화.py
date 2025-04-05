from collections import Counter

n = int(input())
for _ in range(n):
  words = input().replace(" ", "")
  counter = Counter(words).most_common()

  if len(counter) >= 2 and counter[0][1] == counter[1][1]:
    print("?")
  else:
    print(counter[0][0])