def solution(keymap, targets):
    answer = []

    for target in targets:
        value = 0
        for i in range(len(target)):
            min = 0
            for j in range(len(keymap)):
                if target[i] in keymap[j]:
                    index = keymap[j].index(target[i])
                    if min == 0 or min > index + 1:
                        min = index + 1

            if min == 0:
                value = -1
                break
            else:
                value = value + min
        answer.append(value)

    return answer


print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
