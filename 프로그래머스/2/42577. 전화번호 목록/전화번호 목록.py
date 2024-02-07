def solution(phone_book):
    dict = {}
    for num in phone_book:
        for i in range(1, len(num)):
            dict[num[:i]] = 1
            
    for num in phone_book:
        if num in dict:
            return False
    return True