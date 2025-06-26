def solution(today, terms, privacies):
    
    answer = []
    today_year, today_month, today_day = map(int, today.split("."))
    today = 28 * 12 * today_year + 28 * today_month + today_day
        
    def transform(date, num):
        year, month, day = map(int, date.split("."))
            
        return year * 12 * 28 + month * 28 + day + num * 28
        
    dic = {}
    for term in terms:
        privacy, month = term.split()
        dic[privacy] = int(month)
        
    for idx, privacy in enumerate(privacies):
        date, term = privacy.split()
        transformed = transform(date, dic[term])
        if today >=transformed:
            answer.append(idx+1)
    return answer