def solution(ineq, eq, n, m):
    if ineq == "<":
        if eq == "=":
            return int(n <= m)
        elif eq == "!":
            return int(n < m)
    else:
        if eq == "=":
            return int(n >= m)
        elif eq == "!":
            return int(n > m)
            