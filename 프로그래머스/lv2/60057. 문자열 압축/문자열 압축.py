def solution(s):
    answer = int(1e9)
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        string = ''
        cnt = 1
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+2*i]:
                cnt += 1
            else:
                if (cnt != 1):
                    string += str(cnt)
                string += s[j:j+i]
                cnt = 1

        answer = min(answer, len(string))

    return answer