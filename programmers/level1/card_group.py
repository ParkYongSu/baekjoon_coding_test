def solution(cards1, cards2, goal):
    for word in goal:
        is_pop = False

        if len(cards1) > 0 and word == cards1[0]:
            cards1.pop(0)
            is_pop = True
        elif len(cards2) > 0 and word == cards2[0]:
            cards2.pop(0)
            is_pop = True

        if not is_pop:
            return "No"

    return "Yes"


print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
