word = input()
answer = ""

if all(i.islower() or i == "_" for i in word) and word[-1] != "_" and word[0] != "_" and "__" not in word:   # C++ -> Java
  word = word.split("_")
  for i in range(len(word)):
    if i == 0: continue
    word[i] = word[i].capitalize()
  print(''.join(word))
elif "_" not in word and word[0].islower():    # Java -> C++
  for i in range(len(word)):
    if word[i].isupper():
      answer += "_" + word[i].lower()
    else:
      answer += word[i]
    
  print(answer)
else:
  print("Error!")