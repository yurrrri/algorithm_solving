from collections import defaultdict

def solution(genres, plays):
    play_dic = defaultdict(int)  # 장르별 재생수를 저장하기 위한 딕셔너리
    dic = defaultdict(list) # 장르별 노래번호, 재생수 기록할 딕셔너리
    answer = []
    
    for i in range(len(genres)):
        play_dic[genres[i]] += plays[i]
        
    for i in range(len(genres)):  # 장르별 노래 번호, 재생수 기록
        dic[genres[i]].append((i, plays[i]))
        
    sorted_by_play = sorted(play_dic.items(), key=lambda x:x[1], reverse=True) # 재생수가 가장 많은 장르 순으로 정렬
    for genre, play in sorted_by_play:
        arr = [e[0] for e in sorted(dic[genre], key=lambda x:(-x[1], x[0]))]  # 재생수가 많은 대로, 같으면 고유번호 오름차순
        answer += arr[:min(len(arr),2)]
        
    return answer