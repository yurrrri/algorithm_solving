from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_total_dic = defaultdict(int)      # 장르 별 총 재생횟수를 저장할 딕셔너리
    genre_play_dic = defaultdict(list)      # 장르별 (고유번호, 재생횟수) 튜플을 저장할 딕셔너리
    for i, (genre, play) in enumerate(zip(genres, plays)):
        play_total_dic[genre] += play
        genre_play_dic[genre].append((i, play))
        
    sorted_play_total = sorted(play_total_dic, key=lambda x:-play_total_dic[x])
    
    for genre in sorted_play_total:
        _sorted = sorted(genre_play_dic[genre], key=lambda x:(-x[1], x[0]))[:2]
        for i, _ in _sorted:
            answer.append(i)

    return answer