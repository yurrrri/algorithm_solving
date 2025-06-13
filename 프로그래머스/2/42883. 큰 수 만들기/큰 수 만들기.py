def solution(number, k):
    answer = ''
    stack = []
    number = list(number)
    
    for n in number:
        if len(stack) == 0:
            stack.append(n)
            continue
        
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)
    
    if k > 0:
        stack = stack[:len(number)-k]
            
    return "".join(stack)