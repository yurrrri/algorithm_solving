import Foundation

func solution(_ word:String) -> Int {
    var data:[String] = []
    
    func find(_ depth: Int, _ current: String) {
        if depth == 6 { return }
        data.append(String(current))
        
        for i in ["A", "E", "I", "O", "U"] {
            find(depth+1, current + String(i))
        }
    }
    
    find(0, "")
    
    for i in 0..<data.count {
        if data[i] == word {
            return i
        }
    }
    
    return 0
}