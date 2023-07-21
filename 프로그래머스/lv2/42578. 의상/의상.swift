import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dic:[String:Int] = [:]
    var answer = 1
    
    for cloth in clothes {
        dic[cloth[1], default: 0] += 1
    }
    
    for (k, v) in dic {
        answer *= (v+1) // 해당 카테고리에서 하나도 선택하지 않는 경우까지 포함하여 곱함
    }
    return answer-1  // (모자1, 안경1), (모자2, 안경1), (모자1, X), (모자2, X), (안경1, X), (X, X) 라는 경우의 수가 생기므로 여기서 하나도 입지 않는 (X, X)의 개수=1 을 빼면 정답
}