def solution(routes):
    routes.sort(key = lambda x: (x[0], x[0] - x[1]))
    cam = []
    for start, end in routes:
        insert = False
        for i, r in enumerate(cam):
            if start <= r[1]:
                cam[i][0] = start
                cam[i][1] = min(end, r[1])
                insert = True
                break
        if not insert:
            cam.append([start, end])
    return len(cam)