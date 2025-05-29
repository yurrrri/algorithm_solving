def solution(data, ext, val_ext, sort_by):
    answer = []
    
    def extToIndex(ext):
        if ext == "code":
            return 0
        elif ext == "date":
            return 1
        elif ext == "maximum":
            return 2
        else:
            return 3
    
    for d in data:
        if d[extToIndex(ext)] < val_ext:
            answer.append(d)
        
    return sorted(answer, key=lambda x:x[extToIndex(sort_by)])