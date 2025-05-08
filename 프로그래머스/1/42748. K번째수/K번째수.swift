import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer:[Int] = []
    for command in commands {
        let (i, j, k) = (command[0], command[1], command[2])
        answer.append(array[i-1...j-1].sorted()[k-1])
    }
    return answer
}