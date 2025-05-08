import Foundation

let word = readLine()!
let n = word.count
var answer = ""

var r = 0, c = 0
for i in 1...n {
  if n % i == 0 {
    if i <= n / i {
      r = i
      c = n / i
    }
  }
}

var arr = Array(repeating: Array(repeating: "", count: c), count: r)
var idx = 0
for i in 0..<c {
  for j in 0..<r {
    arr[j][i] = String(word[idx])
    idx += 1
  }
}

for i in 0..<r {
  for j in 0..<c {
    answer += arr[i][j]
  }
}

print(answer)

extension String {
  subscript(_ idx: Int) -> Character {
    return self[self.index(self.startIndex, offsetBy: idx)]
  }
}