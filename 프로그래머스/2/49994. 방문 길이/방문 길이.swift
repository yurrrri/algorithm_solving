import Foundation

func isValidArea(_ x: Int, _ y: Int) -> Bool {
    return (-5 <= x && x <= 5) && (-5 <= y && y <= 5)
}

func solution(_ dirs:String) -> Int {
    var cordSet: Set<String> = []
    let offset = ["U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)]
    var nx = 0, ny = 0   // (0, 0) 위치에서 시작
    var x = 0, y = 0
    
    for dir in dirs {
        nx = x + offset[String(dir)]!.0
        ny = y + offset[String(dir)]!.1
        
        if isValidArea(nx, ny) {
            cordSet.insert("\(nx)\(x) \(ny)\(y)")
            cordSet.insert("\(x)\(nx) \(y)\(ny)")
            x = nx
            y = ny
        }
    }

    return cordSet.count / 2
}