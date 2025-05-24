import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    flag = True
    n = int(input())
    nums = []
    for _ in range(n):
        tmp = input().strip()
        nums.append(tmp)
    nums.sort()
    for n1, n2 in zip(nums, nums[1:]):
        if n2.startswith(n1):
            flag = False
    if flag == True:
        print("YES")
    else:
        print("NO")