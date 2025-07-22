def solution(bandage, health, attacks):
    t, x, y = bandage      # 1초마다 x만큼의 체력 회복, t초 연속으로 회복을 성공하면 y만큼의 체력을 추가 회복
    last_time = attacks[-1][0]
    attack_idx = 0          # 공격 idx
    contentious_time = 0    # 연속 붕대 감는 성공 시간
    current_health = health
    
    for time in range(1, last_time+1):        
        if time == attacks[attack_idx][0]:        # 공격 당했을 때
            contentious_time = 0                   # 연속 성공 초기화
            current_health -= attacks[attack_idx][1]
            attack_idx += 1
            if current_health <= 0:    # 체력이 0이하가 되어 죽는다면 -1 return
                return -1
            continue
            
        contentious_time += 1
        current_health += x
        
        if contentious_time == t:   # 연속 성공시, y만큼 추가 회복 및 연속 성공 초기화
            current_health += y
            contentious_time = 0
            
        if current_health >= health:       # 현재 체력이 최대 체력보다 커지는것은 불가능하므로, 최대 체력으로 만들어줌
            current_health = health
    
    return current_health