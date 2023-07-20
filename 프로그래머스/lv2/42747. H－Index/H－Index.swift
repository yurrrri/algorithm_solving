import Foundation

func solution(_ citations:[Int]) -> Int {
    var answer = -1
    
    for cite in 0...citations.max()! {
        let count = citations.filter { $0 >= cite }.count
        if count >= cite && (citations.count - count) <= cite {
            answer = max(answer, cite)
        }
    }
    
    return answer
}