def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    linked = [costs[0][0], costs[0][1]]
    ans = costs[0][2]
    while len(linked) < n:
        for n1, n2, cost in costs:
            if n1 in linked and n2 not in linked:
                linked.append(n2)
                ans += cost
                break
            elif n1 not in linked and n2 in linked:
                linked.append(n1)
                ans += cost
                break
            else:
                continue
    return ans