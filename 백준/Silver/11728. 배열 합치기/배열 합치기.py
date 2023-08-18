import sys

input = sys.stdin.readline
n, m = map(int, input().rstrip().split()) # 배열 A의 크기, B의 크기
a_arr = list(map(int, input().rstrip().split()))
b_arr = list(map(int, input().rstrip().split()))

sorted = sorted(a_arr + b_arr)
print(' '.join(list(map(str, sorted))))