def check(num):  # 나쁜 수열인지 판단
    length = len(num)
    for idx in range(1, length//2 + 1):  # 인접한 2개의 부분 수열이 동일한 것이 존재한다면 나쁜수열
        if num[-idx:] == num[-(idx*2):-idx]:
            return False
    else:
        return True

def dfs(num):
    global n, res

    if len(num) == n:
        print(num)
        exit()
    for i in '123':  # 작은 수는 1, 2, 3, 순서대로 가야하는데 재귀는 1 -> 2 -> 3 순서를 보장함
        if check(num + i):   # 좋은 수열중에
            dfs(num + i)
    return

n = int(input())
dfs('1')