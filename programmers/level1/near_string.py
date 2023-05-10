def solution(s):
    answer = []
    temp = {}

    for i in range(len(s)):
        if s[i] not in temp:
            answer.append(-1)
        else:
            answer.append(i - temp[s[i]])
        temp[s[i]] = i

    return answer


print(solution("banana"))