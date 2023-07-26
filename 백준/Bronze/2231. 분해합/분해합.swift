import Foundation

let n = Int(readLine()!)!

func simulation() -> Int {
  for i in 1...1_000_000 {
    if i + String(i).map { Int(String($0))! }.reduce(0, +) == n {
      return i
    }
  }
  return 0
}

print(simulation())