import sys

input = sys.stdin.readline
n = int(input())
num = input().rstrip()

print(sum(list(map(int, num))))