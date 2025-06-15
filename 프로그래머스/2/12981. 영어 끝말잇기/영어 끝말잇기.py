def solution(n, words):
    word_set = set()
    
    for i, word in enumerate(words):
        if word in word_set:    # 이미 있는 단어를 말할 때 탈락
            # print(word)
            return [(i%n)+1, (i//n)+1]
        if i != 0 and word[0] != words[i-1][-1]:   # 앞 단어의 뒷글자와 현재 말하는 단어의 앞글자가 다를때 탈락
            # print(word)
            return [(i%n)+1, (i//n)+1]
        word_set.add(word)

    return [0, 0]