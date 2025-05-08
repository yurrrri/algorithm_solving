import Foundation

let word = readLine()!
var answer:[String] = []
for i in 1...word.count {
  answer.append(String(word.suffix(i)))
}

answer.sorted().forEach {
  print($0)
}