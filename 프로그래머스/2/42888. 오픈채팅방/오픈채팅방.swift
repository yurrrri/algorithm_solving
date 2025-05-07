import Foundation

func solution(_ record:[String]) -> [String] {
    var dic:[String: String] = [:]
    var answer: [String] = []
    
    for r in record {
        let command = r.components(separatedBy: " ")
        
        if command[0] == "Enter" || command[0] == "Change" {
            dic[command[1]] = command[2]
        }
    }
    
    for r in record {
        let command = r.components(separatedBy: " ")
        switch command[0] {
            case "Enter":
                answer.append("\(dic[command[1]]!)님이 들어왔습니다.")
            case "Leave":
                answer.append("\(dic[command[1]]!)님이 나갔습니다.")
            default:
            break
        }
    }
    return answer
}