func solution(_ info:[String], _ query:[String]) -> [Int] {
    var answer: [Int] = []
    var db: [String: [Int]] = [:]
    
    // 정보에대한 모든 경우의 수 -> 딕셔너리의 key값
    for s in info {
        let infos = s.components(separatedBy: .whitespaces)
        let languages = [infos[0], "-"]
        let jobs = [infos[1], "-"]
        let careers = [infos[2], "-"]
        let soulFoods = [infos[3], "-"]
        let score = Int(infos[4])!
        
        // 조합
        for lang in languages {
            for job in jobs {
                for career in careers {
                    for food in soulFoods {
                        let key = "\(lang) \(job) \(career) \(food)"
                        if db.keys.contains(key) {  //defaultdic이 시간이 더 오래걸림
                            db[key]?.append(score) // 각각의 key별로 score 저장
                        } else {
                            db[key] = [score]
                        }
                    }
                }
            }
        }
    }
    
    // 딕셔너리 점수순 재정렬
    for origin in db {
        let sortValue = origin.value.sorted()
        db[origin.key] = sortValue
    }
    
    // 쿼리를 키로 점수배열을 가져오고 점수배열을 이진탐색으로 효율적탐색 시도
    query.forEach {
        let excuteQuery = $0.components(separatedBy: .whitespaces)
        
        let lang = excuteQuery[0]
        let job = excuteQuery[2]
        let career = excuteQuery[4]
        let food = excuteQuery[6]
        let score = Int(excuteQuery[7])!
        
        let key = "\(lang) \(job) \(career) \(food)"
        if let matchScores = db[key] { // 해당 key에 해당하는 score를 넘는 가장 상한선을 찾음 -> 만족하면서 score을 넘는 지원자를 찾아야하므로
            // 이진 탐색
            var start = 0
            var end = matchScores.count
            while start < end {   // mid때 멈추지 않으므로 범우가 start < end로 변함
                let mid = (start + end) / 2
                
                if matchScores[mid] >= score {
                    end = mid   // 계속 저장해두고 있음
                } else {
                    start = mid + 1
                }
            }
            answer.append(matchScores.count - start)
            
        } else {  // key에 해당하는 지원자를 못찾았다면, 점수 비교할 필요도 없이 0 추가
            answer.append(0)
        }
        
    }
    return answer
}