def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]

    answer = 0
    for word in babbling:
        temp1 = ""
        temp2 = ""
        for w in word:
            temp1 += w
            if temp1 in can and temp1 != temp2:
                temp2 = temp1
                temp1 = ""

        if len(temp1) == 0:
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa"]	))
