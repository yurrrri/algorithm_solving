def solution(number, k):
    stack = [number[0]]
    number = list(number)
    
    for n in number[1:]:
        while stack and stack[-1] < n and k:
            k -= 1
            stack.pop()
        stack.append(n)
    
    if k > 0:   # k를 모두 쓰지않았을 경우
        stack = stack[:len(number)-k]
            
    return "".join(stack)