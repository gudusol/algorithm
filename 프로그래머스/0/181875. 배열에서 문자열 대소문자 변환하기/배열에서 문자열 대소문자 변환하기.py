def solution(strArr):
    for i in range(len(strArr)):
        string = strArr[i]
        if i % 2 == 0:
            strArr[i] = string.lower()
        else:
            strArr[i] = string.upper()
    return strArr