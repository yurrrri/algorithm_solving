from itertools import product

def solution(users, emoticons):
    answer = []
    discount_list = [10, 20, 30, 40]    # 할인율은 10, 20, 30, 40으로 설정
    combinations = product(discount_list, repeat=len(emoticons))     # 각 이모티콘 별 모든 할인률 조합
        
    for combi in combinations:             # 모든 이모티콘 별 할인 조합마다
        join, user_prices = 0, [0] * len(users)     # 이모티콘 플러스 가입, 이모티콘 총 구매 금액을 구하여 answer 배열에 후보지로 추가한다.
        for i, emoji_discount in enumerate(combi):
            for u in range(len(users)):
                if emoji_discount >= users[u][0]:     # 각 이모티콘의 할인율이 각 유저가 생각하는 할인율보다 크거나 같을 경우
                    user_prices[u] += emoticons[i] * (1 - emoji_discount / 100)     # 해당 이모티콘을 구매함
                    
        for i, price in enumerate(user_prices):
            if price >= users[i][1]:      # 유저마다 이모티콘 총 구매 가격이 유저가 생각하는 마지노선 가격보다 크거나 같다면, 이모티콘 플러스를 구매하고 모든 이모티콘에 대한 구매를 취소한다.
                join += 1          # 이모티콘 플러스 구매
                user_prices[i] = 0   # 해당 유저의 모든 이모티콘 구매금액 취소
                
        total = sum(user_prices)       # 모든 이모티콘 구매금액 구하기
        answer.append([join, total])    # 후보지 answer에 추가
        
    return max(answer, key=lambda x:(x[0], x[1]))     # 후보지 중에, 문제 조건대로 이모티콘 플러스 서비스 가입자가 최대인 순으로 정렬하고 이후에 이모티콘 판매량이 가장 큰 경우의 후보지를 선택한다.