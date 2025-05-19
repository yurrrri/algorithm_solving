def solution(players, callings):
    player_rank = {}   # key-value: 선수-순위
    rank_player = {}   # key-value: 순위-선수
    
    for i, player in enumerate(players):
        player_rank[player] = i + 1
        rank_player[i+1] = player
        
    for call in callings:
        call_rank = player_rank[call]   # 불린 말의 현재 순위
        former = rank_player[call_rank-1]  # 앞 플레이어
        former_rank = call_rank - 1     # 앞 플레이어 순위
        
        # 순서 바꾸기
        player_rank[call] = former_rank
        rank_player[former_rank] = call
        
        player_rank[former] = call_rank
        rank_player[call_rank] = former
    
    return sorted(player_rank.keys(), key=lambda x:player_rank[x])