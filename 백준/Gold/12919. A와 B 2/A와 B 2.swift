import Foundation

let s = readLine()!
var t = readLine()!

func backtrack(_ str: String) {  
  if str == s {
    print(1)
    exit(0)
  }
  
  if str.count <= s.count { //s보다 크기가 작아지면 return
    return
  }
  
  if str.last! == "A" {
    var tmp = str
    tmp.removeLast()
    backtrack(tmp)
  } 
  
  if str.first! == "B" {
    var tmp = str
    tmp = String(tmp.reversed())
    tmp.removeLast()
    backtrack(tmp)
  }
}

backtrack(t)
print(0)