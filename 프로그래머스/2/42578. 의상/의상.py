def solution(clothes):
    dict = {}
    for cloth in clothes:
        key = cloth[1]
        if key in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    val = dict.values()
    new_val = [i + 1 for i in val]
    answer = 1
    for i in new_val:
        answer *= i
    return answer -1