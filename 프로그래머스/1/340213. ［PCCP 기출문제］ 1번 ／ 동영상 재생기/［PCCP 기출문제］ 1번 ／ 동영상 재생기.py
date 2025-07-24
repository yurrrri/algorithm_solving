def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def transform(time):
        minute, second = map(int, time.split(":"))
        return minute * 60 + second
    
    video_len = transform(video_len)
    pos = transform(pos)
    op_start = transform(op_start)
    op_end = transform(op_end)
        
    for c in commands:
        if op_start <= pos <= op_end:
            pos = op_end
            
        if c == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
        else:
            pos += 10
            if pos > video_len:
                pos = video_len
                
        if op_start <= pos <= op_end:
            pos = op_end
                
    answer = f"{pos // 60:02d}:{pos % 60:02d}"
                
    return answer