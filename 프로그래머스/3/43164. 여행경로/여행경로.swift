import Foundation

func solution(_ tickets:[[String]]) -> [String] {
    
    var answer:[[String]] = []
    var visited:[Bool] = Array(repeating: false, count: tickets.count)
    
    func dfs(_ airport: String, _ arr: [String]) {
        
        if arr.count == tickets.count + 1 {
            answer.append(arr)
            return
        }
        
        for (idx, ticket) in tickets.enumerated() {
            if ticket[0] == airport && !visited[idx] {
                visited[idx] = true
                dfs(ticket[1], arr + [ticket[1]])
                visited[idx] = false
            }
        }
    }
    
    dfs("ICN", ["ICN"])
    answer = answer.sorted { $0.joined() < $1.joined() }
    
    return answer[0]
}