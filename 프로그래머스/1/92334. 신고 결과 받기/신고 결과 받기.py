def solution(id_list, report, k):
    answer = []
    stopped_id = set()
    user_report = {}
    reported = {}
    for id in id_list:
        user_report[id] = set()
        reported[id] = set()
    
    for report_data in report:
        user_id, report_id = list(report_data.split(' '))
        reported[report_id].add(user_id)
        user_report[user_id].add(report_id)
            
    for report_id in reported:
        if len(reported[report_id]) >= k:
            stopped_id.add(report_id)
    
    for id in id_list:
        answer.append(len(stopped_id & user_report[id]))

    return answer