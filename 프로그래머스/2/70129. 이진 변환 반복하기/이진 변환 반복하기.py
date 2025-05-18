def solution(s):
    bin_count = 0
    zero_count = 0
    
    def s_to_bin(n):
        answer = ""
        while n != 0:
            answer += str(n%2)
            n = n//2
        return answer[::-1]
    
    while s != "1":
        bin_count += 1
        zero_count += s.count("0")
        while "0" in s:
            s = s.replace("0", "")
        length = len(s)
        s = s_to_bin(length)
    return [bin_count, zero_count]