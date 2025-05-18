# def solution(s):
#     bin_count = 0
#     zero_count = 0
    
#     def s_to_bin(n):
#         answer = ""
#         while n != 0:
#             answer += str(n%2)
#             n = n//2
#         return answer[::-1]
    
#     while s != "1":
#         bin_count += 1
#         zero_count += s.count("0")
#         while "0" in s:
#             s = s.replace("0", "")
#         length = len(s)
#         s = s_to_bin(length)
#     return [bin_count, zero_count]

def solution(s):
    bin_count = 0
    zero_count = 0
    
    while s != "1":       # s가 1이 될 때까지 반복
        bin_count += 1       # 이진 변환을 수행한 횟수
        zero_count += s.count("0")   # 변환 과정에서 제거된 모든 0의 갯수
        s = bin(s.count("1"))[2:]   # 1의 갯수를 세고, 해당 수를 이진수로 변환
        
    return [bin_count, zero_count]