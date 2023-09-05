import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answer:[Int] = []
    var progresses = progresses
    var speeds = speeds
    var count = 0
    
    while !progresses.isEmpty {
        for i in 0..<progresses.count {
            progresses[i] += speeds[i]
        }
        count = 0
        while !progresses.isEmpty && progresses.first! >= 100 {
            count += 1
            progresses.removeFirst()
            speeds.removeFirst()
        }
        if count > 0 {
            answer.append(count)
        }
    }
    return answer
}