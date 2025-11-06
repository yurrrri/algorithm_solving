def solution(record):
    answer = []
    dic = {}
    
    for r in record:
        if r.startswith("Enter") or r.startswith("Change"):
            _, userid, name = r.split()
            dic[userid] = name
            
    for r in record:
        if r.startswith("Enter"):
            _, userid, _ = r.split()
            answer.append(f"{dic[userid]}님이 들어왔습니다.")
        elif r.startswith("Leave"):
            _, userid = r.split()
            answer.append(f"{dic[userid]}님이 나갔습니다.")
        
    return answer