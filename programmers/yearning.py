def solution(name, yearning, photo):
    yearning_dic = {}
    for i in range(len(name)):
        yearning_dic[name[i]] = yearning[i]
    answer = []
    for e in photo:
        score = 0
        for name in e:
            if name in yearning_dic.keys():
                score += yearning_dic[name]
        answer.append(score)

    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))