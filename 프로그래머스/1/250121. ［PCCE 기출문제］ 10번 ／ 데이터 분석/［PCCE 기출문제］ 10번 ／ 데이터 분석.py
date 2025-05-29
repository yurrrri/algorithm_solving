def solution(data, ext, val_ext, sort_by):
    answer = []
    axis=["code", "date", "maximum", "remain"]
    
    for d in data:
        if d[axis.index(ext)] < val_ext:
            answer.append(d)
        
    return sorted(answer, key=lambda x:x[axis.index(sort_by)])