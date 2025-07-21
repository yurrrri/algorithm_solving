from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    
    def check(_id, standard):
        if len(_id) != len(standard):
            return False
        
        for u, s in zip(_id, standard):
            if s == "*":
                continue
            if u != s:
                return False
            
        return True
    
    C = permutations(user_id, len(banned_id))
    for users in C:
        flag = True
        for u, b in zip(users, banned_id):
            if not check(u, b):
                flag = False
                break
        if flag:
            sorted_list = sorted(list(users))
            if sorted_list not in answer:
                answer.append(sorted_list)
    return len(answer)