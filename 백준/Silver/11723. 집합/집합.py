import sys
input = sys.stdin.readline
n = int(input())
_set = set()

for _ in range(n):
  command = input().rstrip().split()
  if command[0] == "add":
    _set.add(int(command[1]))
  elif command[0] == "remove":
    if int(command[1]) in _set:
      _set.remove(int(command[1]))
  elif command[0] == "check":
    if int(command[1]) in _set:
      print(1)
    else:
      print(0)
  elif command[0] == "toggle":
    if int(command[1]) in _set:
      _set.remove(int(command[1]))
    else:
      _set.add(int(command[1]))
  elif command[0] == "all":
      _set = {x for x in range(1, 21)}
  else:
      _set = set()
