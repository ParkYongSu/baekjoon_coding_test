def solution(t, p):
    count = 0
    for i in range(len(t) - (len(p) - 1)):
        sub = t[i: i + len(p)]
        print(sub)
        if int(sub) <= int(p):
            count += 1
    return count


print(solution("10203", "15"))