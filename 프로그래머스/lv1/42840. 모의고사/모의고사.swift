import Foundation

func solution(_ answers:[Int]) -> [Int] {
    var answer:[Int] = []
    var maxValue = 0
    
    // 노트1. repeating을 배열 기준으로 할 수 있다.
    var firstArr = Array(repeating: [1, 2, 3, 4, 5], count:10000/5).flatMap { $0 }
    var secondArr = Array(repeating: [2, 1, 2, 3, 2, 4, 2, 5], count:10000/8).flatMap { $0 }
    var thirdArr = Array(repeating: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], count:10000/10).flatMap { $0 }
    
    var first = 0, second = 0, third = 0
    
    for i in 0..<answers.count {
        if firstArr[i] == answers[i] {
            first += 1
        }
        
        if secondArr[i] == answers[i] {
            second += 1
        }
        
        if thirdArr[i] == answers[i] {
            third += 1
        }
    }
    
    maxValue = [first, second, third].max()!
    
    return [(1, first), (2, second), (3, third)].filter { $0.1 == maxValue }.map { $0.0 }
}