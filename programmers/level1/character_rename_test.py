def solution(survey, choices):
    scores = [3, 2, 1, 0, 1, 2, 3]
    result = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):
        s = survey[i]
        choice = choices[i] - 1
        if choice > 3:
            result[s[1]] += scores[choice]
        elif choice < 3:
            result[s[0]] += scores[choice]

    result_items = list(result.items())
    answer = ''

    for j in range(4):
        if result_items[0][1] < result_items[1][1]:
            answer += result_items[1][0]
        else:
            answer += result_items[0][0]
        result_items = result_items[2:]

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [4, 4, 4, 4, 4]	))
