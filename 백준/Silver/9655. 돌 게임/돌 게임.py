n = int(input())
i = -1

while n > 0:
  i += 1
  
  if n > 3:
    n -= 3
  else:
    n -= 1

if i%2 == 0:
  print("SK")
else:
  print("CY")