from collections import deque

def solution(skill, skill_trees):
    answer = 0
#     skill = list(skill)
#     for s in skill_trees:
#         stack = []
#         for a in s:
#             if a in skill and skill.index(a) >= 1:
#                 if not skill[skill.index(a)-1] in stack:
#                     break
#             stack.append(a)

#         if len(stack) == len(s):
#             answer += 1
    for skills in skill_trees:
        skill_list = deque(list(skill))
        
        for s in skills:
            if s in skill and s != skill_list.popleft():
                break
        else:
            answer += 1

    return answer