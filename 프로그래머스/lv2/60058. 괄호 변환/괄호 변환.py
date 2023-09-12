def check(st): # 올바른 괄호 문자열인지 확인하는 함수
    stack = []
    stack.append(st[0])
    
    for s in st[1:]:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == "(" and s == ")":
                stack.pop()
            else:
                stack.append(s)
            
    if not stack:   # 위 절차를 거치고 스택이 비었으면 --> 올바른 문자열
        return True
    else:
        return False

def dfs(string):
    if not string: # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
        return string
    
    close = 0
    for i in range(len(string)):
        if string[i] == "(":
            close += 1
        else:
            close -= 1
        
        if close == 0: #2. u는 균형잡힌 괄호 문자열로 더이상 분리할 수 없어야 함 (i까지 자른 문자열이 u)
            u = string[:i+1]
            v = string[i+1:]
            if check(u):  # 3. 문자열 u가 올바르괄호 문자열이라면, v 재귀
                return ''.join([u, dfs(v)])
            else:
                make = ["(", dfs(v), ")"]
                
                for j in range(1, i):
                    if u[j] == "(":
                        make.append(")")
                    else:
                        make.append("(")
                return ''.join(make)
                
def solution(p):
    return dfs(p)