import Foundation

var arr:[Int] = []
for _ in 0..<9 {
  arr.append(Int(readLine()!)!)
}
arr.sort()

func combinations(_ idx: Int, _ combi: [Int]){  
  if combi.count == 7 && combi.reduce(0, +) == 100  {
    print(combi.sorted().map { String($0) }.joined(separator:"\n"))
    exit(0)
  }

  for i in idx..<arr.count {
    combinations(i+1, combi + [arr[i]])
  }
}

combinations(0, [])