def solution(record):
    dic = {}
    result = []
    
    for r in record:
        if not r.startswith("Leave"):
            command, uid, nickname = r.split()
            dic[uid] = nickname
            
    for r in record:
        if r.startswith("Enter"):
            command, uid, nickname = r.split()
            result.append(f"{dic[uid]}님이 들어왔습니다.")
        elif r.startswith("Leave"):
            command, uid = r.split()
            result.append(f"{dic[uid]}님이 나갔습니다.")
    
    return result