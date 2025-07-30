answer = 0

documents = input()
word = input()
n = len(word)
  
i = 0

while i+n <= len(documents):
  if documents[i:i+n] == word:
    answer += 1
    i += n
  else:
    i += 1

print(answer)