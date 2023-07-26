import Foundation

let n = Int(readLine()!)!
var triangleArr:[Int] = []

for i in 1...44 {
  triangleArr.append((i*(i+1))/2)
}

func simulation(_ n: Int) -> Int {
  for i in 0..<44 {
    for j in 0..<44 {
      for k in 0..<44 {
        if triangleArr[i] + triangleArr[j] + triangleArr[k] == n {
          return 1
        }
      }
    }
  }
  return 0
}

for _ in 0..<n {
  print(simulation(Int(readLine()!)!))
}