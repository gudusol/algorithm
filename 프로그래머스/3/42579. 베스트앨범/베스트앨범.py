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
        ans += id_list[:min(len(id_list), 2)]
    return ans