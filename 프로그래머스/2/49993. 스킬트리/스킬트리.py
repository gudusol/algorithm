def solution(skill, skill_trees):
    skill_tree = { s: index for index, s in enumerate(skill)}
    
    trees = [[skill_tree[s] for s in tree if s in skill_tree] for tree in skill_trees]
    
    answer = 0
    for t in trees:
        cur_skill = 0
        impossible = False
        
        for sk in t:
            if cur_skill != sk:
                impossible = True
                break
            cur_skill += 1
            
        if not impossible:
            answer += 1
            
    return answer