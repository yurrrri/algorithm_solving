def solution(m, musicinfos):
    
    def change(x):		# #음 치환
        exc = {'C#':'c','D#':'d', 'F#':'f', 'G#':'g', 'A#':'a', 'B#': 'b'}
        for k, v in exc.items():
            x = x.replace(k, v)
        return x

    def calculate_minute(t1, t2):
        t1 = t1.split(":")
        t2 = t2.split(":")
        
        hour, minute = (0, 0)
        hour = int(t2[0]) - int(t1[0])
        minute = int(t2[1]) - int(t1[1])
        
        if minute < 0:
            hour -=1
            minute += 60
            
        return hour * 60 + minute
                
    
    answers = []
    m = change(m)
    
    for music in musicinfos:
        start, end, title, info = music.split(",")
        duration = calculate_minute(start, end)
        info = change(info)
        played = (info * (duration // len(info))) + info[:duration % len(info)]
        if m in played:
            answers.append((title, duration))
            
    if not answers:
        return "(None)"
    else: 
        answers.sort(key=lambda x:-x[1])   # 재생시간 순으로 내림차순, 같으면 입력 순서대로 (유지)
        return answers[0][0]