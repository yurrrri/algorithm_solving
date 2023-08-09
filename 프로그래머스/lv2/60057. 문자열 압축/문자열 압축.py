def solution(s):
    answer = int(1e9)
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        string = ''
        cnt = 1
        for j in range(0, len(s), i):
            comp = s[j:j+i]
            """
            오답노트
            j가 len(s)까지 가는데 왜 10번째줄에서 인덱스 에러가 나지 않을까?
            파이썬에서는 인덱스 초과 접근 시 에러가 나지만, 슬라이스에서는 알아서 초과되지 않는 범위에서 잘라준다.
            """
            if comp == s[j+i:j+2*i]:
                cnt += 1
            else:
                if (cnt != 1):
                    string += str(cnt)
                string += comp
                cnt = 1

        answer = min(answer, len(string))

    return answer