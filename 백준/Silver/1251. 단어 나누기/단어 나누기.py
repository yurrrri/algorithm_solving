word = input()
_len = len(word)
arr = []

for i in range(1, _len-1):   # 1 2 3 4 5
  for j in range(i+1, _len): # 2 3 4 5 6
    arr.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

print(sorted(arr)[0])