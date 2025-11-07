from collections import deque

def solution(msg):
    answer = []
    dic = {}
    for i in range(26):
        dic[chr(ord('A')+i)] = i+1   # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    msg = deque(msg)
    number = 26
        
    while msg:
        poped = msg.popleft()
        
        while msg and poped + msg[0] in dic:  # 2. 사전에서현재 입력과 일치하는 가장 긴 문자열 w를 찾는다
            poped += msg.popleft()
        answer.append(dic[poped])    # 3. 색인번호 출력 후, 입력에서 w 제거
        
        if msg:     # 4. 처리되지 않은 다음 글자가 남아있다면, 
            number += 1
            dic[poped + msg[0]] = number    # w+c에 해당하는 단어를 사전에 등록한다. (이때 제거하는게 아니므로 pop하지 말것)
    return answer