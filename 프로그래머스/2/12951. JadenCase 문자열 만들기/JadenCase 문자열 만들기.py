import re

def solution(s):
    answer = []
    arr = re.split(r'( )', s)
    for c in arr:
        answer.append(c.lower().capitalize())
    return "".join(answer)