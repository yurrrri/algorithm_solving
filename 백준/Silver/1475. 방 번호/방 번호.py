num = list(map(int, input()))
arr = [0] * 10

for n in num:
  if n == 6:
    if arr[9] < arr[6]:
      arr[9] += 1
    else:
      arr[6] += 1
  elif n == 9:
    if arr[6] < arr[9]:
      arr[6] += 1
    else:
      arr[9] += 1
  else:
    arr[n] += 1  

print(max(arr))