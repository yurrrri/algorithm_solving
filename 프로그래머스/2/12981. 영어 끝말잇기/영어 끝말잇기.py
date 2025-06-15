def solution(n, words):
    word_set = set()
    
    for i, word in enumerate(words):
        if word in word_set:
            # print(word)
            return [(i%n)+1, (i//n)+1]
        if i != 0 and word[0] != words[i-1][-1]:
            # print(word)
            return [(i%n)+1, (i//n)+1]
        word_set.add(word)

    return [0, 0]