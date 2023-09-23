from collections import Counter

n = int(input())
counter = Counter(list(input())).most_common()
if len(counter) > 1 and counter[0][1] == counter[1][1]:
  print("Tie")
else:
  print(counter[0][0])