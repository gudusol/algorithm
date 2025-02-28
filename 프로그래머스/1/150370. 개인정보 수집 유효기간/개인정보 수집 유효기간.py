def solution(today, terms, privacies):
    today_year, today_month, today_day = map(int, today.split('.'))
    today_date = today_year * 12 * 28 + today_month * 28 + today_day
    answer = []
    expire_date = []
    terms_date = {}
    for term in terms:
        name, month = term.split(' ')
        terms_date[name] = int(month)
    
    for privacy in privacies:
        start_date, term = privacy.split(' ')
        year, month, date = map(int, start_date.split('.'))
        expire_date.append(year * 12 * 28 + month * 28 + date + terms_date[term] * 28)
    
    for idx in range(len(expire_date)):
        if today_date >= expire_date[idx]:
            answer.append(idx + 1)
    
    return answer