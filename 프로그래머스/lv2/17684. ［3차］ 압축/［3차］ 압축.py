def solution(msg):
    idx_list = []
    word_dict = {}
    
    for i in range(0, 26):   # 길이가 1인 A ~ Z까지 들어있는 사전 초기화
        word_dict[chr(ord('A') +  i)] = i+1  # 색인 / 문자
        
    idx = 26
    while msg:
        temp = ''
        for i in range(1, len(msg)+1):
            # 입력이 사전에 없는 경우
            temp = msg[:i]
            if temp not in word_dict:
                idx += 1
                word_dict[temp] = idx   # 사전에 인덱스 새로 등록
                temp = temp[:-1]
                idx_list.append(word_dict[temp])
                break
        msg = msg[len(temp):]  # msg에서 이전단어(temp) 제거
        if not msg:   # 마지막응로 처리되지 않은 글자가 있다면 해당 글자의 색인번호 추가
            idx_list.append(word_dict[temp])
    return idx_list