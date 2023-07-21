def solution(phone_book):
#     phone_book.sort()
    
#     for i in range(len(phone_book)-1):
#         if phone_book[i+1].startswith(phone_book[i]):
#             return False
    
#     return True
    dic = {}
    
    for phone_number in phone_book:
        dic[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in dic and temp != phone_number:
                return False
    return True