def solution(genres, plays):
    dic = {}
    ans = []
    play_list = [(i, plays[i]) for i in range(len(plays))]
    play_list.sort(key=lambda x:x[1], reverse=True)
    
    for id, play in play_list:
        genre = genres[id]
        if genre in dic:
            dic[genre]['total'] += play
            dic[genre]['list'].append(id)
        else:
            dic[genre] = {"total": play, "list": [id]}
            
    sorted_dict = sorted(dic.items(), key = lambda x:x[1]['total'], reverse=True)

    for genre, value in sorted_dict:
        id_list = value['list']
        
        count = 0
        for id in id_list:
            if count == 2:
                break
            ans.append(id)
            count += 1
    return ans