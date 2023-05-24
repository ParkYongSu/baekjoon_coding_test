def solution(id_list, report, k):
    reported_num = {name: 0 for name in id_list}
    report_list = {name: [] for name in id_list}
    stop = set()

    for r in set(report):
        e = r.split()
        if e[1] not in report_list[e[0]]:
            report_list[e[0]].append(e[1])
            reported_num[e[1]] += 1
            if reported_num[e[1]] >= k:
                stop.add(e[1])

    mail_num = {name: 0 for name in id_list}

    for s in stop:
        for e in report_list:
            if s in report_list[e]:
                mail_num[e] += 1

    return list(mail_num.values())


print(
    solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
             2))
