import Foundation

let input = readLine()!.split(separator:" ").map { Int($0)! }
let l = input[0], c = input[1]
// 최소 1개의 모음과 2개의 자음, 알파벳순 정렬
let letters = readLine()!.split(separator:" ").map { String($0) }.sorted()
var visited = Array(repeating: false, count: c)
let moeum = ["a", "e", "i", "o", "u"]
var answer:[String] = []

func isValidLetter(_ str: [String]) -> Bool {
  var moeum_count = 0
  var jaeum_count = 0
  
  for i in str {
    if moeum.contains(i) {
      moeum_count += 1
    } else {
      jaeum_count += 1
    }
  }

  return moeum_count >= 1 && jaeum_count >= 2
}

func backtracking(_ start: Int) {
  if answer.count == l {
    if isValidLetter(answer) {
      print(answer.joined())
    }
    return
  }

  for i in start..<c {
    if !visited[i] {
      visited[i] = true
        answer.append(letters[i])
       backtracking(i)
      answer.removeLast() 
      visited[i] = false
    }
  }
}

backtracking(0)