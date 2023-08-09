def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        else:
            start = ord('a') if s[i].islower() else ord('A')
            corr = (ord(s[i]) + n - start) % 26 + start
            answer += chr(corr)
    return answer