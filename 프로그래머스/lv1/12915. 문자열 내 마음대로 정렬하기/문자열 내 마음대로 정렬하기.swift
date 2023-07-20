func solution(_ strings:[String], _ n:Int) -> [String] {
    
    if strings.count == 1 {
        return strings
    }
    
    var sorted:[String] = []
    sorted = strings.sorted(by: { 
        if $0[n] < $1[n] {  // 인덱스 1의 문자가 더 앞서면 더 앞
            return true
        } else if $0[n] == $1[n] {
            return $0 < $1
        } else {
            return false
        }
    })
    
    return sorted
}

extension String {
    subscript (_ index: Int) -> String {
        return String(self[self.index(self.startIndex, offsetBy: index)])
    }
}