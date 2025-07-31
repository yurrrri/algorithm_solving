from collections import deque

t = int(input())
for _ in range(t):
  n = int(input())
  words = input().split()
  cards = deque([words.pop(0)])

  for w in words:
    if w <= cards[0]:
      cards.appendleft(w)
    else:
      cards.append(w)

  print("".join(cards))