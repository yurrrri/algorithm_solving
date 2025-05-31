n = int(input())
keys = []

for _ in range(n):
  words = input()
  answer = ""
  
  for i, w in enumerate(words):
    if (i == 0 and w.upper() not in keys) or (words[i-1] == " " and w.upper() not in keys) and "[" not in answer:
      keys.append(w.upper())
      answer += "[" + w + "]"
    else:
      answer += w

  if "[" in answer:
    print(answer)
    continue

  answer = ""

  for w in words:
    if w.isalpha() and w.upper() not in keys and "[" not in answer:
      keys.append(w.upper())
      answer += "[" + w + "]"
    else:
      answer += w

  if "[" in answer:
    print(answer)
    continue

  print(words)