from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_total_playtimes = defaultdict(int)
    genre_playtimes = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres, plays)):    # 장르별 가장 많이 재생된 노래를 찾기 위한 딕셔너리
        genre_total_playtimes[g] += p
        genre_playtimes[g].append((i, p))     # 장르별 노래의 고유번호, 플레이횟수
        
    for genre in sorted(genre_total_playtimes, key=lambda x:-genre_total_playtimes[x]):   # 장르별 총 재생횟수를 내림차순으로 정렬한 키값 리스트
        answer.extend([i for i, _ in sorted(genre_playtimes[genre], key=lambda x:(-x[1], x[0]))][:2])
    
    
    return answer