import sys

input = sys.stdin.readline
words = input().rstrip()
while words != "END":
  print(words[::-1])
  words = input().rstrip()