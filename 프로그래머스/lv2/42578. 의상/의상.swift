import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dic:[String:Int] = [:]
    var answer = 1
    
    for cloth in clothes {
        dic[cloth[1], default: 0] += 1
    }
    
    for (k, v) in dic {
        answer *= (v+1)
    }
    return answer-1
}