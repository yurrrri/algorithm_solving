def solution(n, k, cmd):
    stack = []   # 삭제된 인덱스를 저장하는 리스트 (가장 최근에 삭제된 행으로 연산하므로 스택 활용)

    # 각 행 위아래의 행의 인덱스를 저장하는 리스트
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 1)]

    k += 1    # 위 아래로 임시공간을 늘렸으므로, 초기에 1을 더한 것이 처음 시작임

    for c in cmd:
        if c.startswith("C"):     # C: 행 삭제
            stack.append(k)       # 삭제한 인덱스 추가
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]

        elif c.startswith("Z"):     # 가장 최근에 삭제한 행 복구
            restore = stack.pop() 
            down[up[restore]] = restore
            up[down[restore]] = restore

        # U 또는 D: 위 혹은 아래로 이동
        else:
            action, num = c.split( ) 
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]

    answer = ["O"] * n
    for i in stack:
        answer[i - 1] = "X"
    
    return "".join(answer)