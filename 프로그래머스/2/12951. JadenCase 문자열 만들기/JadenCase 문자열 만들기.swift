import Foundation

func solution(_ s: String) -> String {
    let arr = s.split(separator: " ", omittingEmptySubsequences: false).map { String($0) }
    var answer: [String] = []

    for word in arr {
        if let first = word.first {
            if first.isLetter {
                answer.append(word.lowercased().capitalized)
            } else {
                answer.append(word.lowercased())
            }
        } else {
            answer.append("") // 공백만 있는 요소 처리
        }
    }

    return answer.joined(separator: " ")
}