import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var stages_counter:[Int: Int] = [:]
    var failes: [Int: Double] = [:]
    for stage in stages {
        stages_counter[stage, default:0] += 1
    }
    var total = stages.count
    let stages = stages.sorted()
    var answer:[Int] = []
    
    for i in 1...N {
        if let count = stages_counter[i] {
            failes[i] = Double(count) / Double(total)
            total -= count
        } else {
            failes[i] = 0.0
        }
    }
    
    let sortedDic = failes.sorted {
        if $0.value == $1.value {
            return $0.key < $1.key  // 실패율 같으면 key 기준 오름차순
        }
        return $0.value > $1.value // 실패율 기준 내림차순
    }
    
    for (key, value) in sortedDic {
        answer.append(key)
    }
    
    return answer
}