word = list(input())
alphabets = [0] * 26
for c in word:
  alphabets[ord(c) - ord('a')] += 1
for a in alphabets:
  print(a, end=" ")