def listToDict(list):
    dict = {}
    for key in list:
        if key in dict:
            dict[key] = dict[key] + 1
        else:
            dict[key] = 1
    return dict


def solution(participant, completion):
    p_dict = listToDict(participant)
    c_dict = listToDict(completion)

    for key in p_dict:
        if (key not in c_dict) or c_dict[key] < p_dict[key]:
            return key
