import Foundation

let n = Int(readLine()!)!
var arr:[Int] = []
var count = 0
var num = 666

while true {
  var c = 0
  for i in String(num) {
    if i == "6" {
      c+=1

      if c == 3 {
        break
      }
    } else {
      c = 0
    }
  }

  if c == 3 {
    count += 1
  }

  if count == n {
    print(num)
    break
  }

  num += 1
}