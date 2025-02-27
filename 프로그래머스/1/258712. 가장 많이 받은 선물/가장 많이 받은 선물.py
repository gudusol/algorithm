def solution(friends, gifts):
    answer = []
    give = {}
    take = {}
    score = {}
    
    for friend in friends:
        give[friend] = {f:0 for f in friends}
        take[friend] = {f:0 for f in friends}
        score[friend] = 0
    

        
    for data in gifts:
        giver, taker = data.split(' ')
        give[giver][taker] += 1
        take[taker][giver] += 1
    
    for friend in friends:
        score[friend] = sum(give[friend].values()) - sum(take[friend].values())
    
    for me in friends:
        me_score = 0
        for friend in friends:
            if me != friend:
                give_count = give[me][friend]
                take_count = give[friend][me]
                if give_count > take_count:
                    me_score += 1
                elif give_count == take_count:
                    if score[me] > score[friend]:
                        me_score += 1
        answer.append(me_score)
    return max(answer)