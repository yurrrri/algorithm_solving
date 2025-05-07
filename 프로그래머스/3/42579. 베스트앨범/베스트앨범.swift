import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var totalDic: [String:Int] = [:]
    var playDic: [String: [(Int, Int)]] = [:]
    var answer:[Int] = []
    
    for (index, genre) in genres.enumerated() {
        playDic[genre, default:[]].append((index, plays[index]))  // 장르별 (고유번호, 재생수)
        totalDic[genre, default:0] += plays[index]   // 장르별 총 재생수
    }
    
    let sortedTotalDic = totalDic.sorted(by: { $0.1 > $1.1 })   // 가장 많이 재생된 장르 순서대로 정렬
    
    for (k, v) in sortedTotalDic {
        let sortedPlayDic = playDic[k]!.sorted {
            if $0.1 == $1.1 {
                return $0.0 < $1.0
            } else {
                return $0.1 > $1.1
            }
        }.prefix(2)
        answer.append(contentsOf: sortedPlayDic.map { $0.0 })
    }
    
    
    return answer
}