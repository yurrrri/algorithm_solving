import Foundation

func recursive(node: Int, visited: inout [Bool], graph: [[Int]], count: inout Int) {
    visited[node] = true
    count += 1
    
    let canGos = graph[node]
    canGos.forEach {
        if !visited[$0] {
            recursive(node: $0, visited: &visited, graph: graph, count: &count)
        }
    }
}

let numInfo = readLine()!.split(separator: " ").map { Int(String($0))! }
let nodeNum = numInfo[0]
let edgeNum = numInfo[1]

var graph: [[Int]] = .init(repeating: [], count: nodeNum)
//var graph: [[Bool]] = .init(repeating: .init(repeating: false, count: nodeNum), count: nodeNum)

(0..<edgeNum).forEach { _ in
    let row = readLine()!.split(separator: " ").map { Int(String($0))! }
//    graph[row[1] - 1][row[0] - 1] = true
    graph[row[1] - 1].append(row[0] - 1)
}

var maxCount = 0
var result: [Int] = []

for node in 0..<nodeNum {
    
    var visited: [Bool] = .init(repeating: false, count: nodeNum)
    var count = 0
    recursive(node: node, visited: &visited, graph: graph, count: &count)
    
    if count > maxCount {
        result = [node + 1]
        maxCount = count
    } else if count == maxCount {
        result.append(node + 1)
    }
}

print(result.map { String($0) }.joined(separator: " "))