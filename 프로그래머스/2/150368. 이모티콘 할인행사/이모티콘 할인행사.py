def solution(users, emoticons):
    answer = []
    discount_list = [10, 20, 30, 40]
    combinations = []
    
    def dfs(arr, depth):
        if len(arr) == depth:
            combinations.append(arr[:])
            return
        
        for discount in discount_list:
            arr[depth] += discount
            dfs(arr, depth+1)
            arr[depth] -= discount
            
    dfs([0] * len(emoticons), 0)
        
    for combi in combinations:       # 이모티콘 별 할인률 조합 별로
        join, user_prices = 0, [0] * len(users)
        for i, emoji_discount in enumerate(combi):
            for u in range(len(users)):
                if emoji_discount >= users[u][0]:
                    user_prices[u] += emoticons[i] * (1 - emoji_discount / 100)     
                    
        for i, price in enumerate(user_prices):
            if price >= users[i][1]:
                join += 1
                user_prices[i] = 0
                
        total = sum(user_prices)
        answer.append([join, total])
        
    return max(answer, key=lambda x:(x[0], x[1]))