func solution(_ info:[String], _ query:[String]) -> [Int] {
    var result: [Int] = []
    var db: [String: [Int]] = [:]
    
    // 정보에대한 모든 경우의 수 입력해놓기
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
                        if db.keys.contains(key) {
                            db[key]?.append(score)
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
        if let matchScores = db[key] {
            // 이진 탐색
            var start = 0
            var end = matchScores.count
            while start < end {
                let mid = (start + end) / 2
                
                if matchScores[mid] >= score {
                    end = mid
                } else {
                    start = mid + 1
                }
            }
            result.append(matchScores.count - start)
            
        } else {
            result.append(0)
        }
        
    }
    return result
}