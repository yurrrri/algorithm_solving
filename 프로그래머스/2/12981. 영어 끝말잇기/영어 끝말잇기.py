def solution(n, words):
    words_set = set()
    for i in range(len(words)):
        if words[i] in words_set or (words_set and words[i][0] != words[i-1][-1]):
            return [(i%n)+1, (i//n)+1]
            
        words_set.add(words[i])

    return [0, 0]