def solution(genres, plays):
    dic = {}
    count_dic = {}
    answer = []
    
    for i in range(len(genres)):
        if not genres[i] in dic:
            dic[genres[i]] = []
            count_dic[genres[i]] = 0
        dic[genres[i]].append((i, plays[i]))
        count_dic[genres[i]] += plays[i]
        
    sorted_genres = sorted(count_dic.items(), key=lambda x:x[1], reverse=True)
    
    for genre, _ in sorted_genres:
        temp = sorted(dic[genre], key=lambda x:(-x[1], x[0]))
        answer.extend([idx for idx, _ in temp[:2]])
            
    return answer