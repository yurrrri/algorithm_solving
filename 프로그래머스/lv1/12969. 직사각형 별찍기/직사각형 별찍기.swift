import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])

var string = ""
for i in 1...b {
    for j in 1...a {
        string += "*"
    }
    string += "\n"
}

print(string)