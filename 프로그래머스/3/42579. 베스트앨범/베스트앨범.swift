import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var totalDic: [String:Int] = [:]
    var playDic: [String: [(Int, Int)]] = [:]
    var answer:[Int] = []
    
    for (index, genre) in genres.enumerated() {
        playDic[genre, default:[]].append((index, plays[index]))
        totalDic[genre, default:0] += plays[index]
    }
    
    let sortedTotalDic = totalDic.sorted(by: { $0.1 > $1.1 })
    
    for (k, v) in sortedTotalDic {
        let sortedPlayDic = playDic[k]!.sorted(by: { $0.1 > $1.1 })
        if sortedPlayDic.count >= 2 {
            answer.append(sortedPlayDic[0].0)
            answer.append(sortedPlayDic[1].0)
        } else {
            answer.append(sortedPlayDic[0].0)
        }
    }
    
    return answer
}